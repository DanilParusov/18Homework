from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import SchemaGenre



genre_schema = SchemaGenre()  # для одного фильма
genres_schema = SchemaGenre(many=True)  # для нескольких фильмов

genre_ns = Namespace('genres')



@genre_ns.route('/')
class GenreView(Resource):
    """ Получение всех жанров """
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    """ Получение по id """
    def get(self, uid: int):
        genre = genre_service.get_one(uid)
        if not genre:
            return "Жанр не найден", 404
        return genre_schema.dump(genre), 200