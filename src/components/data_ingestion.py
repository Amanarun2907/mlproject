import os # operating system module
import sys ## system module

from src.exception import CustomException ## exception handling 
from src.log_config import logging ## log config file
import pandas as pd ## pandas 
import numpy as np ## numpy
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer
@dataclass ## by this there is no need to write init method
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self): ## constructor 
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self): ## function 
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('Notebook\data\stud.csv') ## reading the local csv file  
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) ## creating the directory if not exists (artifacts folder)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) ## saving the raw data 

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42) ## train test split

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) ## saving the training file 

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) ## saving the testing file 

            logging.info("Inmgestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e: ## use of exception handling
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion() 

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



