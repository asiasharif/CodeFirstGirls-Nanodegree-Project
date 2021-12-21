from flask import render_template, redirect, url_for, request, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from project.models import User
from project import db
from project.movie_data import MovieAPI


def login():
    return render_template('index.html')


def login_form():
    password = request.form.get('password')
    email = request.form.get('email')
    remember = True if request.form.get('remember') else False

    if len(email) and len(password) > 0:

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Incorrect login details. Please input your details again.')
            return redirect(url_for('auth.login_form'))
        login_user(user, remember=remember)
        return redirect(url_for('main.homepage'))
    else:
        flash('Please enter your login details before you submit')
        return redirect(url_for('auth.login_form'))


def signup():
    return render_template('signup.html')


def signup_form():
    email = request.form.get('email')
    password = request.form.get('password')

    if len(email) and len(password) > 0:

        user = User.query.filter_by(email=email).first()

        if user:
            flash('This email address is already taken')
            return redirect(url_for('auth.signup'))

        new_user = User(email=email, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        flash('Please enter your signup details before you submit')
        return redirect(url_for('auth.signup'))


@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


auth = Blueprint('auth', __name__)

auth.add_url_rule('/', view_func=login)
auth.add_url_rule('/', view_func=login_form, methods=["POST"])
auth.add_url_rule('/signup', view_func=signup)
auth.add_url_rule('/signup', view_func=signup_form, methods=["POST"])
auth.add_url_rule('/logout', view_func=logout)
auth.add_url_rule('/movie', view_func=MovieAPI.as_view('movie'))
