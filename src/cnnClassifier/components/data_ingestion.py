import py7zr
#update the components 

import os
import urllib.request as request   #to download the dataset 
import zipfile  #to unzip the data
from src.cnnClassifier import logger  
from src.cnnClassifier.utils.common import get_size  #for seeing the data size 
from src.cnnClassifier.entity.config_entity import DataIngestionConfig # importing the DataIngestionConfig class from config_entity.py file
from pathlib import Path  #to create the path for the data

class DataIngestion:   #to get the components 
    def __init__(self, config: DataIngestionConfig):
        self.config = config    #it will take config of the data ingestion 


    
    def download_file(self):   #download the file from the URL
        if not os.path.exists(self.config.local_data_file):  #if the file does not exist then download it
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}") #logging the info of the file downloaded
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        source_path = self.config.local_data_file
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with py7zr.SevenZipFile(source_path, mode='r') as archive:
            archive.extractall(path=unzip_path) #extract all the files in the zip file to the unzip path