import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# imports the env.py file if it exists
# as this is in the .gitignore, we will be using heroku to generate 
# this for us
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# setting SQL Alchemy database to the instance of our Flask app
db = SQLAlchemy(app)

from taskmanager import routes