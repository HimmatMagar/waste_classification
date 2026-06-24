from wasteClassification import logger
from wasteClassification.config import ConfigManager
from wasteClassification.components.model_eval import ModelEval


STAGE_NAME = "Model Eval Stage"

class ModelEvalPipeline:

      def __init__(self):
            pass
      
      def main(self):
            config = ConfigManager()
            eval_config = config.getModelEvalConfig()

            model_eval = ModelEval(eval_config)
            model_eval.evaluate_model()

if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvalPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 