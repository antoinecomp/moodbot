from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import json
import os
#import psycopg2

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Introduction to Flask-Login
from flask_login import LoginManager

# for new Database
#from config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

#for chatbot
import random

# for database
#DATABASE_URL = os.environ.get('DATABASE_URL')


app = Flask(__name__)

login = LoginManager(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

if __name__ == '__main__':
	# must be changed
    app.secret_key='secret123'
    # db.init_app(app)
    port = int(os.environ.get("PORT", 5000))
    #app.run(port=8000,debug=True)
    app.run(host='0.0.0.0', port=port)
