from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        self.logger = logger
        self.logger.info(f"Starting {STAGE_NAME} pipeline")

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e