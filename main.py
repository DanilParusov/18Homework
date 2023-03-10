from flask import Flask
from flask_restx import Api

from app.config import Config
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

if __name__ == '__main__':
    app = create_app(Config())
    app.run(debug=True)
