# --*--coding: utf-8 --*--
# @Time: 2023-05-26 23:57
# @Author: 李月初
# @FIle: __init__
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'

db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'login'


@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


from dmwatchlist import views, errors, commands
from dmwatchlist.models import User, Movie