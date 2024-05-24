from cnnClassifier import logger
from cnnClassifier.pipelines.stage_01_data_ingestion import DataIngeestionTrainingPipeline
from cnnClassifier.exception import CustomException

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngeestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x ============= x")
except Exception as e:
    CustomException(e, sys)

