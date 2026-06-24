from src.wasteClassification import logger
from src.wasteClassification.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.wasteClassification.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.wasteClassification.pipeline.model_eval_pipeline import ModelEvalPipeline


# STAGE_NAME = "Data Ingestion Stage"
# try:
#       logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#       obj = DataIngestionPipeline()
#       obj.main()
#       logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e


# stage_name = "Model Training Stage"
# try:
#       logger.info(f">>>>>> {stage_name} started <<<<<<")
#       obj = ModelTrainingPipeline()
#       obj.Train_Model()
#       logger.info(f">>>>>> {stage_name} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e

STAGE_NAME = "Model Eval Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = ModelEvalPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e