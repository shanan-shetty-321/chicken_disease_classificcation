from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml,create_directories   
#currently humlog chicken_disease_classification ke andhar hai it can directly read from utils as immediate andhar mein voh file nhi hai 
# as src is inside chicken_disease_classification  then src.cnnclassifier means src ke andhar cnnclassifier ke andhar waalo ko access kartha hai 
from src.cnnClassifier.constants import *
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig,# importing the DataIngestionConfig class from config_entity.py file
                                                    PrepareBaseModelConfig) # importing the PrepareBaseModelConfig class from config_entity.py file
class ConfigurationManager:
    def __init__(    #for creating root folders and subfolders for data ingestion 
        self,
        config_filepath = CONFIG_FILE_PATH,   # path to the config file importing from constants.py
        params_filepath = PARAMS_FILE_PATH):    # path to the params file importing from constants.py

        self.config = read_yaml(config_filepath) # reading the config file
        self.params = read_yaml(params_filepath) # reading the params file

        create_directories([self.config.artifacts_root]) # creating the root directory for artifacts


    
    def get_data_ingestion_config(self) -> DataIngestionConfig: 
        config = self.config.data_ingestion  #storing the config data which is in config.yaml in a variable

        create_directories([config.root_dir]) # creating the root directory for data ingestion in artifacts 

        data_ingestion_config = DataIngestionConfig(  #creating the data ingestion config object where u r reading the data from config.yaml file
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config # return all configuration related to our data ingestion 

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
    
    