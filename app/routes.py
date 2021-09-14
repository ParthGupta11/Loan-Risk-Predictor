from flask import render_template, url_for, request
from app import app
from app import categories
import pickle
import numpy as np
import pandas as pd


full_pipeline = pickle.load(open('my_pipeline.pkl', 'rb'))

prof_list = categories.professions
city_list = categories.cities
state_list = categories.states

def fetch_features(form):
    '''
    reads data from the html form and returns array of feature values on which prediction will be made
    '''
    # creating data frame
    df = pd.DataFrame()

    # getting values from the html form
    df['Income'] = [int(form.get("income"))]
    df['Age'] = [int(form.get("age"))]
    df['Experience'] = [int(form.get("exp"))]
    df['Married/Single'] = [form.get("maritalStatus")]
    df['House_Ownership'] = [form.get("house")]
    df['Car_Ownership'] = [form.get("car")]
    df['Profession'] = [form.get("prof")]
    df['CITY'] = [form.get("city")]
    df['STATE'] = [form.get("state")]
    df['CURRENT_JOB_YRS'] = [int(form.get("currentjobyears"))]
    df['CURRENT_HOUSE_YRS'] = [int(form.get("currenthouseyears"))]

    return df



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', state_list=state_list, prof_list=prof_list, city_list=city_list)


@app.route('/prediction', methods=["POST"])
def prediction():
    if request.method == "POST":
        
        X_test = fetch_features(request.form)

        flag_pred = full_pipeline.predict(X_test)

        return render_template('index.html', state_list=state_list, prof_list=prof_list, city_list=city_list, flag = flag_pred)

    return render_template('index.html', state_list=state_list, prof_list=prof_list, city_list=city_list)


@app.route('/details')
def details():
    return render_template('details.html')
