from dataclasses import dataclass
from pathlib import Path

        #this is the entity (DataIngestionConfig) #


@dataclass(frozen=True)    ## Makes the class immutable (values cannot be changed after creation) to prevent accidental modification
class DataIngestionConfig:
    root_dir:Path  ## Main directory for data ingestion
    source_URL:str   # # URL of the dataset
    local_data_file:Path   # Path to the downloaded dataset file
    unzip_dir:Path       # Directory where extracted files will be stored
    
    
    

@dataclass(frozen=True)
class PrepareBaseModelConfig:   
    #taking data from the config file
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    #taking data from params.yaml file
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int