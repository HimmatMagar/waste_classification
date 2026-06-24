from wasteClassification import logger
from wasteClassification.entity import *
from wasteClassification.constants import *
from wasteClassification.utils import *


class ConfigManager:

    def __init__(self, config = config, params = params):
        self.config = read_yaml(config)
        self.params = read_yaml(params)
    
        create_dir([self.config.root])
    

    def getDataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dir([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            zip_file=config.zip_file,
            unzip_file=config.unzip_file
        )
    
    def getModelBuildingConfig(self) -> ModelBuildingConfig:
            config = self.config.model_building
            create_dir([config.root_dir])

            return ModelBuildingConfig(
                  root_dir = config.root_dir,
                  train_data_file = config.train_data_file,
                  model = config.model
            )
    

    def getModelEvalConfig(self) -> ModelEvalConfig:
        config = self.config.model_evaluation
        create_dir([config.root_dir])

        return ModelEvalConfig(
            root_dir=config.root_dir,
            test_data_file=config.test_data_file,
            model=config.model,
            metrices=config.metrices
        )