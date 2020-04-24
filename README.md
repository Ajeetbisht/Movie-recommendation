# Movie recommendations system

This is a demo project to make a real world recomendations system

Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

# Project Structure
This project has four major parts :

1. model.py - This contains code fot our Machine Learning model to recommend you from your history.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to  interact with the web app .
Running the project
Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage as below : alt text

If everything goes well, you should be able to get movie recommendation from flask app.
