from wasteClassification import logger
from wasteClassification.entity import *
from wasteClassification.constants import *
from wasteClassification.utils import *


class ConfigManager:

    def __init__(self, config = config, params = params):
        self.config = read_yaml(config)
        self.params = read_yaml(params)
    
        create_dir([self.config.root])