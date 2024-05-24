import os
import pandas as pd
import numpy as np
from box.exceptions import BoxValueError
from yaml import safe_load
from src.mlproject import logger
import json
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV
import joblib
from ensure import ensure_annotations 
import sys
from cnnClassifier.exception import CustomException
from box import ConfigBox #ease access of values from dictionary (d.key1) instead of d["key1"]
from pathlib import Path
from typing import Any 
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = safe_load(yaml_file) #will return dictionary
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        logger.info(f"json file saved at: {path}")
    except Exception as e:
        CustomException(e, sys)




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    try:
        with open(path) as f:
            content = json.load(f)

        logger.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        CustomException(e, sys)



@ensure_annotations
def evaluate_models(X_train, y_train,X_test,y_test,models,param):

    """Evaluate models using GridSearchCV

    Args:
        path (Path): path to json file
        X_train: X_train object
        y_train: X_train object
        X_test: X_test object
        y_test: y_test object
        models: list of models
        param: dict of hyperparameters of the model.

    Returns:
        r2_score, MAE, RSME: Evaluation metrics of the model.
    """
    try:
        report_r2 = {}
        report_mae = {}
        report_rmse = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model=model,
                            param_grid=para,
                            cv=5,
                            scoring='r2',
                            error_score='raise',
                            n_jobs=-1)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_r2_score = r2_score(y_train, y_train_pred)
        
            test_r2_score = r2_score(y_test, y_test_pred)
            test_mae = mean_absolute_error(y_test, y_test_pred)
            test_mse = mean_squared_error(y_test, y_test_pred)
            test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

            report_r2[list(models.keys())[i]] = test_r2_score
            report_mae[list(models.keys())[i]] = test_mae
            report_rmse[list(models.keys())[i]] = test_rmse

        return report_r2, report_mae, report_rmse
    
    except Exception as e:
        CustomException(e, sys)



@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"binary file saved at: {path}")
    except Exception as e:
        CustomException(e, sys)


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(path)
        logger.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        CustomException(e, sys)



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        CustomException(e, sys)


def decodeImage(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
            f.close()
    except Exception as e:
        CustomException(e, sys) 



def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
    except Exception as e:
        CustomException(e, sys)