from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    raise e