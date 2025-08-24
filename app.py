import pickle 
from flask import Flask,request,render_template ## flask is a micro web framework written in python . 
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler 
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__) ## entry point for the flask application

app=application

## Route for a home page

@app.route('/')
def index():
    ## it will search for the template folder and then it will search for index.html file and it will render the index.html file
    return render_template('index.html')  ## index.html file is in the template folder

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint(): ## this function is also used in home.html file . 
    if request.method=='GET':
        return render_template('home.html') ## home.html file is in the template folder this file contains the simple input data field that our model is required to give  the prediction . 
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')))
        
        pred_df=data.get_data_as_data_frame() ## function is present in predict_pipeline.py file
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df) ## transformation + prediction 
        return render_template('home.html',results=results[0])  ## return statements 
    
    

if __name__=="__main__":      
    # app.run(host="0.0.0.0",port=80)   
    app.run(debug=True)  # For development purposes, use debug=True


# http://127.0.0.1:5000/predictdata
# http://127.0.0.1:5000/