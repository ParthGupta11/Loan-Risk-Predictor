# Loan Risk Predictor

The project uses machine learning to classify whether granting loan to a particular customer is safe or risky. 

It uses **XGBoost Classifier** to make predictions on data and is deployed as a web app using **Flask framework**. The classifer has been optimized over the ROC AUC metrics and gives a score of 0.86. 

## Structure of the Project

The content of the repository are as follows

*  app - Folder containing the flask app code.

    * static - folder containing images and CSS for the website.
    * templates - folder of HTML files that are rendered.
    * routes - python code file of the backend created using flask.
    * categories - python file containing list of categories for the categorical variables in the html form.
    * init - python file used to initialize a module. It creates the flask app object

* Loan Defaulter Prediction - jupyter notebook that was used to carry out _data analysis_, _feature engineering_, and _modelling_ of the machine learning classifier.

* my_pipeline - pickle file of the _machine learning pipeline_ that is used to preprocess and make predicitions of the user input

* Data - csv file of the data over which the model was trained and tested. Source - [Kaggle](https://www.kaggle.com/subhamjain/loan-prediction-based-on-customer-behavior)


* run - python file that imports the flask app object from the app module and runs it on the local server, in the debug mode.

* requirements - a .txt file that lists all the required packages for running the flask app and viweing the jupyter notebook

## Installing the Project

1. Download all the files in the repository
2. Install all the required packages in your python environment listed in requirements.txt file
    * using pip
```console
pip install -r requirements.txt
```
* using conda
```console
conda create --name <env_name> --file requirements.txt
```

3. Open terminal/anaconda prompt and activate the environment with required packages.
4. Enter the root directory.

## Running the Flask app on the local server
To run the app, run the following command on terminal
```console
python run.py
```
If everything runs correctly, the output will be
```console
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 181-754-048
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 Copy the url and paste and open it on a web browser. You can now see the website running. 

 Try it out by filling the form with customer details and getting the risk predictions!