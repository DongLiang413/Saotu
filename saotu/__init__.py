# -*- encoding=UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from saotu import views, models

app = Flask(__name__)
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)

