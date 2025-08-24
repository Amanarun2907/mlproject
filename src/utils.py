import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV ## for hyperparameter tunning
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
def evaluate_models(X_train, y_train,X_test,y_test,models ,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3) ##GridSearchCV is used for hyperparameter tunning
            ## cv is the cross validation parameter here i have taken 3 fold cross validation , para = parameter , model = model name
            gs.fit(X_train,y_train) ## model fitting 

            model.set_params(**gs.best_params_) ## set the best parameters
            model.fit(X_train,y_train) ## model fitting

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train) ## predict the training data

            y_test_pred = model.predict(X_test) ## predict the testing data

            train_model_score = r2_score(y_train, y_train_pred) ## R Square score for training data

            test_model_score = r2_score(y_test, y_test_pred) ## R Square score for testing data

            report[list(models.keys())[i]] = test_model_score 

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)