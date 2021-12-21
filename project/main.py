from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user

alchemy_db = SQLAlchemy()

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html', name=current_user.name)
