from unittest.mock import MagicMock

import pytest

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title="Movie", description="about movie", trailer="hgf", year=2000, rating=20.5)
    m2 = Movie(id=2, title="Movie", description="about movie", trailer="hgf", year=2000, rating=20.5)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2])
    movie_dao.create = MagicMock(return_value=Movie(id=1))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "SkyPro",
            "description": "hgf",
            "trailer": "hgfc",
            "year": 2000,
            "rating": 20.9
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 2,
            "title": "SkyPro",
            "description": "hgf",
            "trailer": "hgfc",
            "year": 2000,
            "rating": 20.9
        }
        self.movie_service.update(movie_d)
