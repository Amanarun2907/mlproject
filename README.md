## End to End Machine learning project 

## Step 1 :Setting virtual environment

pip install virtualenv

python -m venv .venv

.venv\Scripts\activate

## Step 2 : Create github repository and add a relation of github with local machine. and also make a README.md file in it.

## Step 3 : Make a .gitignore file in the github repository itself . 

## Step 3 : Make a requirements.txt file in the root directory.

## Step 4 : Make a setup.py file in the root directory.

## Step 5 : Make a src folder in the root directory and create an __init__.py file inside that folder. 

## Step 6 : Make a file of logging and exeception handling in the src folder by logging.py and exception.py files respectively. and run them using these commands : python src/log_config.py and python src/exception.py 

##  Step 7 : Here we have to upload the dataset in data folder and doing the part of model training and eda part in notebook folder under the .ipynb file. 

## Step 8 : Now here we have to work on the data ingestion part so for this we have to create a new file named as data_ingestion.py in the src folder and then write all the code related to data ingestion there.

## Step 9 : Now we will work on the data_transformation part so for this we have to create a new file named as data_transformation.py in the src folder and then write all the code related to data transformation there.


## Step 10 : Now we will work on the model_trainer part so for this we have to create a new file named as model_trainer.py in the src folder and then write all the code related to model trainer there.

## Step 11 : Hyper Parameter part of the Model is taking place in this step and we have made changes in src/utils.py file , src/components/data_ingestion.py and src/components/model_trainer.py files accordingly.