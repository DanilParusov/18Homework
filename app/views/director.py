from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import SchemaDirector

director_schema = SchemaDirector()  # для одного фильма
directors_schema = SchemaDirector(many=True)  # для нескольких фильмов

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    """ Получение всех режиссеров """

    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    """ Получение по id """

    def get(self, uid: int):
        director = director_service.get_one(uid)
        if not director:
            return "Режиссер не найден", 404
        return director_schema.dump(director), 200
