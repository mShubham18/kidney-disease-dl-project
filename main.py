from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

# Performing Data Ingestion
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    raise e
# Preparing Base model
STAGE_NAME =  "Prepare base model"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
        raise e

STAGE_NAME = "Training"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    raise e



STAGE_NAME = "Evaluation stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
        raise e
