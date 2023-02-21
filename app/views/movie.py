from flask import request, json
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import SchemaMovie


movie_schema = SchemaMovie()  # для одного фильма
movies_schema = SchemaMovie(many=True)  # для нескольких фильмов

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MovieView(Resource):
    """ Получение всех фильмов """

    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200



        # director_id = request.args.get('director_id')
        # genre_id = request.args.get('genre_id')
        # if director_id:
        #     movies = db.session.query(Movie).filter(Movie.director_id == int(director_id)).all()
        #     return movies_schema.dump(movies), 200
        # elif genre_id:
        #     movies = db.session.query(Movie).filter(Movie.genre_id == int(genre_id)).all()
        #     return movies_schema.dump(movies), 200
        #
        # return movies_schema.dump(Movie.query.all()), 200

    """ Добавление фильма """

    def post(self):
        data = json.loads(request.data)

        movie_service.create(data)

        return "", 201


""" Эндпоинт для Movie /movie/{id} """


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """ Получение по id """

    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        if not movie:
            return "Фильм не найден", 404
        return movie_schema.dump(movie), 200

    """ Удаление по id """

    def delete(self, mid: int):
        movie = movie_service.delete(mid)
        return "", 204

    """ Oбновление по id """

    def put(self, mid: int):
        data = json.loads(request.data)
        data["id"] = mid

        movie_service.update(data)

        return "Фильм обновлен", 204

    def patch(self, mid):
        data = json.loads(request.data)
        data["id"] = mid

        movie_service.update_partial(data)

        return "Фильм обновлен", 204