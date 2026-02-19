from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.TextSummarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated") 
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
    
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated") 
    data_ingestion_pipeline = DataTransformationTrainingPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed")
    
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated") 
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} completed")
    
except Exception as e:
    logger.exception(e)
    raise(e)