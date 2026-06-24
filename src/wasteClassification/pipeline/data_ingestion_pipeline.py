from wasteClassification import logger
from wasteClassification.config import ConfigManager
from wasteClassification.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Config"

class DataIngestionPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigManager()
            data_ingestion_config = config.getDataIngestionConfig()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_zip_file()
            data_ingestion.extract_file()

if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 