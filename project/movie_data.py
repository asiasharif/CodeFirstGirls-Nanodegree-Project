from flask import Flask, render_template, request, flash
import requests
from flask.views import MethodView
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("API_KEY")

app = Flask(__name__)


class MovieAPI(MethodView):

    def get(self):
        if request.method == "POST" and len(request.form["searchfilmtitle"]) > 0:
            search_movie_title = request.form["searchfilmtitle"]
            base_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={search_movie_title}&page=1&include_adult=false"
            response = requests.get(base_url)
            moviedb = response.json()
            return moviedb
        else:
            return render_template("homepage.html")

    def post(self):
        try:
            moviedb = self.get()
            if len(moviedb) > 0:
                parseMovieData = {
                    'id': moviedb['results'][0]['id'],
                    'title': moviedb['results'][0]['title'],
                    'overview': moviedb['results'][0]['overview'],
                    'poster_path': f"https://www.themoviedb.org/t/p/w1280{moviedb['results'][0]['poster_path']}",
                    'release_date': moviedb['results'][0]['release_date'],
                }
                id_value = list(parseMovieData.values())
                id_for_recommendations = id_value[0]
                recommendations_url = f'https://api.themoviedb.org/3/movie/{id_for_recommendations}?api_key={api_key}&append_to_response=recommendations'
                response = requests.get(recommendations_url)
                rec_moviedb = response.json()
                rec_list = []
                movie_results = rec_moviedb['recommendations']['results']
                for result in movie_results[:3]:
                    rec_list.append({
                        'title': result["title"],
                        'overview': result['overview'],
                        'poster_path': f"https://www.themoviedb.org/t/p/w1280{result['poster_path']}",
                    })
                return render_template("movie.html", parseMovieData=parseMovieData,
                                       rec_list=rec_list)
            else:
                return render_template("homepage.html")
        except IndexError:
            flash("The movie you searched for is not in our database. Please search for a different movie title.")
            return render_template("homepage.html")
        except TypeError:
            flash("Please enter a movie title before you press enter!")
            return render_template("homepage.html")
