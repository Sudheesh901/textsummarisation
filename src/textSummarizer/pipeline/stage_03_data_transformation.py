from textSummarizer.config.confuiguration import ConfigurationManager
from textSummarizer.entity import DataTransformationConfig
from textSummarizer.components.data_tranformation import DataTransformation
from textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()




