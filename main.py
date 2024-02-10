from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

try:
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"{STAGE_NAME} pipeline completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} pipeline failed with error: {e}")
    raise e