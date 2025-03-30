from dataclasses import dataclass
from pathlib import Path

        #this is the entity (DataIngestionConfig) #


@dataclass(frozen=True)    ## Makes the class immutable (values cannot be changed after creation) to prevent accidental modification
class DataIngestionConfig:
    root_dir:Path  ## Main directory for data ingestion
    source_URL:str   # # URL of the dataset
    local_data_file:Path   # Path to the downloaded dataset file
    unzip_dir:Path       # Directory where extracted files will be stored