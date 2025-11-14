from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

from textSummarizer.logging import logger


STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f"*************")
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Data Validation stage"

try:
    logger.info(f"*************")
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"

try:
    logger.info(f"*************")
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_tranformation=DataTransformationTrainingPipeline()
    data_tranformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training stage"

try:
    logger.info(f"*************")
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    Model_training=ModelTrainingPipeline()
    Model_training.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation stage"

try:
    logger.info(f"*************")
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    Model_evaluation=ModelTrainingPipeline()
    Model_evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========")
except Exception as e:
    logger.exception(e)
    raise e

'''
STSGR_NAME ="Token Generation Stage"

try:
    logger.info(f"*************")
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    token_generation=TokenGenerationPipeline()
    dialogue=input("Enter Agen-customer dialogue")
    result=token_generation.run(dialogue)
    print("\nSummary:", result["summary"])
    print("Tokens:", result["tokens"])
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========")
except Exception as e:
    logger.exception(e)
    raise(e)

'''

