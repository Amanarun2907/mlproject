## End to End Machine learning project 

if you are doing first time then please also pay attention to the git configuration (github username and github email )

git config --global user.email



## Step 1 : Set up a github repository environment 


## Step 2 :Setting virtual environment

pip install virtualenv

python -m venv .venv

.venv\Scripts\activate

## Step 3 : Creating a  README.md file where you can write your discription and important point regarding the project . 


## Step 4 : Create github repository and add a relation of github with local machine. and also make a README.md file in it.

## Step 5  : Make a .gitignore file in the github repository itself .  .gitignore file is created by github platform and use git pull command 

## Step 3 : Make a requirements.txt file in the root directory.

pip install -r requirements.txt

## Step 4 : Make a setup.py file in the root directory. https://pypy.org/ . With the help of setup.py i will able to build  my ml application  as a package  and even deploy in pypy . 

## Step 5 : Make a src folder in the root directory and create an __init__.py file inside that folder. 

1st folder of src folder  : components : data_ingestion.py (reading the data) / data_transformation.py (for data transformation) / model_trainer.py (confusion matriz / r^2 or adjusted r^2 value / training purpose) . modules that we use in our project 

2nd folder of src folder  : pipeline : train_pipeline.py (training pipeline) / predict_pipeline.py (testing pipeline)

## Step 6 : Make a file of logging and exeception handling in the src folder by logging.py and exception.py files respectively. and run them using these commands : python src/log_config.py and python src/exception.py and src/utils.py

logging is done in log_config.py and custom handling is done in exception.py file and it helps us to show the message regarding custom exeception and logging 

Logging : src/log_config.py file is used 
exception : src/exception.py file is used 

##  Step 7 : Here we have to upload the dataset in data folder and doing the part of model training and eda part in notebook folder under the .ipynb file. 

notebook/data/dataset 

#### Life cycle of Machine learning Project

- Understanding the Problem Statement
- Data Collection
- Data Checks to perform
- Exploratory data analysis
- Data Pre-Processing
- Model Training
- Choose best model

- performing exploratory data analysis part and model training here 

- all the steps of exploratory data analysis and model training is done is .ipynb file and then later we will convert it in modular coding .

## Step 8 : Now here we have to work on the data ingestion part so for this we have to create a new file named as data_ingestion.py in the src folder and then write all the code related to data ingestion there.

src/components/data_ingestion.py file is basically used for data_ingestion.py file and in this we have to basically read the dataset from various sources and doing the train test split part too for as 80 percent is training and 20 percent is testing so we have to do all these in data_ingestion.py file . 

## Step 9 : Now we will work on the data_transformation part so for this we have to create a new file named as data_transformation.py in the src folder and then write all the code related to data transformation there.

- src/components/data_tranformation in which we basically first created a numerical pipeline and then we also created a categorical pipeline then we combined both of them and also handle the logging and custom exception too [imputer , column transformer , one hot encoding ......]

## Step 10 : Now we will work on the model_trainer part so for this we have to create a new file named as model_trainer.py in the src folder and then write all the code related to model trainer there.

src/components/model_trainer.py  is used for model training and evaluation and also performed the hyperparameter tunning ..........
- spliting in X_train,X_test , y_train and y_test 
- r^2 square is used as performance matrix here . 
- We have to select the best model which give us maximum value of r^2 value . ..................

## Step 11 : Hyper Parameter part of the Model is taking place in this step and we have made changes in src/utils.py file , src/components/data_ingestion.py and src/components/model_trainer.py files accordingly.

- for hyperparameter tunning we actually focus on the two file 
src/components/model_trainer.py and src/components/utils.py 

## Step 12 : Now we use flask to make an application and work on the predict_pipeline also and if we are using flask then we have to make templates folder too . 

- we have generated a web framework from flask and also make pipeline and connect every important file with each other so that connection should be stable . 
