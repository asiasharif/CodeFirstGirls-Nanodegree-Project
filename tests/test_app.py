from unittest.mock import patch, Mock
from unittest import TestCase, main
import pytest
import requests
import os
from project import create_app
from project.movie_data import MovieAPI
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("API_KEY")


class MovieAPITest(TestCase):

    def test_get_moviedb(self):
        mock_get_request_patch = patch('project.movie_data.requests.get')
        movie = [{
            "id": 15121,
            "title": "The Sound of Music"
        }]

        mock_get_request = mock_get_request_patch.start()

        mock_get_request.return_value = Mock(status_code=200)
        mock_get_request.return_value.json.return_value = movie

        response = requests.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), movie)

    def test_exception_handling(self):
        with self.assertRaises(Exception):
            MovieAPI.post()

    def test_api_url_check_status_code_equals_200(self):
        response = requests.get(f"https://api.themoviedb.org/3/movie/76341?api_key={api_key}")
        assert response.status_code == 200

    def test_api_recommendations_url_check_status_code_equals_200(self):
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/27205?api_key={api_key}&append_to_response=recommendations")
        assert response.status_code == 200


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client


def test_landing_page(client):
    expected_strings = ["Sign Up", "Login"]
    response = client.get('/')
    for string in expected_strings:
        is_matched = True if string in str(response.data) else False
        assert is_matched


def test_homepage(client):
    expected_strings = ["Enter a movie title for recommendations"]
    response = client.get('/movie')
    for string in expected_strings:
        is_matched = True if string in str(response.data) else False
        print(str(response.data))
        assert is_matched


if __name__ == '__main__':
    main()
