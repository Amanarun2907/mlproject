import sys # system 
from dataclasses import dataclass # dataclass

import numpy as np # numpy lib 
import pandas as pd # pandas lib 
from sklearn.compose import ColumnTransformer # one hot encoding + standard scaler + column transformer
from sklearn.impute import SimpleImputer  ## here we are actually handle the missing values as filling the missing values by mean so that handling of the missing values has to be done carefully .  
from sklearn.pipeline import Pipeline # pipeline is done 
from sklearn.preprocessing import OneHotEncoder,StandardScaler # one hot encoding + standard scaler

from src.exception import CustomException ## exception handling is imported from here . 
from src.log_config import logging # log config file as in this file logging is done and  logging is the important part of the project . 
import os ## operating system module

from src.utils import save_object

@dataclass ## by it we not need to initialize __init__ method . it is used as a decorator . 
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()  ## this is initializing the data transformation config class object .

    def get_data_transformer_object(self): ## new function that is created in the data transformation class . 
        '''
        This function is responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"] ## numerical features 
            categorical_columns = [ ## categorical features that has the datatype as object . 
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
## this is my numerical pipeline in which i am handling the numerical column of my dataset by standardization and inputer (mean ) . 
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")), ## it is used to fill the missing values with median [ middle value]
                ("scaler",StandardScaler()) ## formulla : (x-mean)/std deviation 

                ]
            )
## this is my categorical pipeline in which i am handling the categorical column of my dataset by one hot encoding , inputer (mode) and standarization  .
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")), ## it is used to fill the missing values with most frequent value (mode)
                ("one_hot_encoder",OneHotEncoder()), ## one hot encoder
                ("scaler",StandardScaler(with_mean=False)) ## it is used to scale the data but with mean as false because one hot encoding creates dummy variables which are not normally distributed so we don't want to subtract the mean from them. (optional)
                ]

            )
## time for logging message . 
            logging.info(f"Categorical columns: {categorical_columns}")
            
            logging.info(f"Numerical columns: {numerical_columns}")
## combine our numerical and categorical pipeline using column transformer .
            preprocessor=ColumnTransformer(
                ## pipeline name  , what type of pipeline  , which columns is should be applied .
                [
                ("num_pipeline",num_pipeline,numerical_columns), # numerical columns pipeline
                ("cat_pipelines",cat_pipeline,categorical_columns) # categorical columns pipeline
                ]


            )

            return preprocessor # return the preprocessor object
        
        except Exception as e: ## handling the exception
            raise CustomException(e,sys)
## exceptional handling
        
    def initiate_data_transformation(self,train_path,test_path): ## training and testing path is getting from the data_ingestion part . 

        try:
            train_df=pd.read_csv(train_path) ## training data uploading
            test_df=pd.read_csv(test_path) ## testing data uploading 

            logging.info("Read train and test data completed")  ## logging.info is used to log the information

            logging.info("Obtaining preprocessing object") 
## creating a preproceesing object by calling the function get_data_transformer_object
            preprocessing_obj=self.get_data_transformer_object()    ## calling the function get_data_transformer_object

            target_column_name="math_score" ##target variable name (y)
            numerical_columns = ["writing_score", "reading_score"]  ## numerical features

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1) ## basically separating the dependent and independent variable (Training Data) [y_train amd X_train]
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1) ## basically separating the dependent and independent variable (Testing Data) [X_test amd y_test]
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df) ## fit_tranform is used to fit the data and transform it
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df) ## transform is used to transform the data

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
# The use of "c_" in Python programming primarily refers to numpy.c_, a specialized indexing routine within the NumPy library, which is used for efficient array manipulation, particularly for concatenating arrays along the second axis (columns).
            logging.info(f"Saved preprocessing object.")
## by save_object function the preprocessor object is saved in the pkl file .
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
