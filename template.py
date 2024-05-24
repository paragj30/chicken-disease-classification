import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/CICD.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/exception.py",

    f"src/{project_name}/constant/__init__.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    
    "config/config.yaml",
    "secret.yaml",
    "params.yaml",

    f"research/stage_01_data_ingestion.ipynb",
    f"research/stage_02_prepare_base_model.ipynb",
    f"research/stage_03_model_training.ipynb",
    f"research/stage_04_model_evaluation.ipynb",
    f"research/EDA.ipynb",
    f"research/model_training_experiment.ipynb",
    f"research/trials.ipynb",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/prepare_base_model.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_prepare_base_model.py",
    f"src/{project_name}/pipeline/stage_03_model_training.py",
    f"src/{project_name}/pipeline/stage_04_model_evaluation.py",



    "main.py",
    "dvc.yaml",
    "app.py",

    "setup.py",
    "requirements.txt",

    "templates/index.html",
    "templates/results.html",
    "Dockerfile"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")