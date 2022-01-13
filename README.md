# CodeFirstGirls-Nanodegree-Project

# CodeFirstGirls-Nanodegree-Project

# FilmNow Application

Team members: 
* Arpineh Janiyan
* Asia Sharif
* Sulekha Sirad
* Yasmine El-Sayed
* Zodumo Mbuthuma

# Project description: 
FilmNow is a film recommendation system that allows you to enter a movie title of your choice and receive movie info on the film you searched along with three recommendations based on it.


# Requirements:

* Clone this GitHub repository into a folder on your device via terminal.
* Import python-dotenv
* Import SQLAlchemy
* Import flask
* Import flask_login
* Import requests 
* db.sqlite text file - If the db.sqlite (not the db.sqlite.py file) text file is empty, please delete that file and run the db.sqlite.py file. This will then produce the correct db.sqlite text file.
* Register for an API key from The Movie Database (TMDB): https://www.themoviedb.org/documentation/api
* Generate a Secret Key for the Flask login system by writing the following code at the top of one of the Python files:
```python
import os 
SECRET_KEY = os.random(24)
print(SECRET_KEY)
```
Please save your Secret Key and delete the above three lines after you have generated your Secret Key.
* Create .env file in CodeFirstGirls-Nanodegree-Project to add and hide your API_KEY and SECRET_KEY. 

For example, you can write this on the .env file:
```python
API_KEY = <apikey>
SECRET_KEY = <secretkey>
```
* If you would like to hide the .env file, please add it to .gitignore


# How to run this project
To run this, please input in the following commands in the terminal:

Mac users:
 * export FLASK_APP=project 
 * export FLASK_DEBUG=1 
 * flask run

Windows users:
 * $env:FLASK_APP="project"
 * python -m flask run

  
When you are on the application, please sign up (with fake details if you want!) and login.
