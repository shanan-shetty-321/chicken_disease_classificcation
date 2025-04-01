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
    
    

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
    
    

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list



@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int