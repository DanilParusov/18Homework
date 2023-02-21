from flask import Flask
from flask_restx import Api

import data
from app.config import Config
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from app.setup_db import db
from app.views.movie import movie_ns
from app.views.genre import genre_ns
from app.views.director import director_ns

# функция создания основного объекта app
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)

def load_data():
    """ Добавление данных в таблицу Movie """
    for movie in data["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )

    """ Добавление данных в таблицу Director """
    for director in data["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )

    """ Добавление данных в таблицу Genre """
    for genre in data["genres"]:
        g = Genre(
            id=genre["pk"],
            name=genre["name"],
        )

    db.create_all()

    with db.session.begin():
        db.session.add(m)
        db.sessiom.add(d)
        db.session.add(g)



if __name__ == '__main__':
    app = create_app(Config())
    app.run(debug=True)
