from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        return self.dao.update(movie_d)

    def partially_update(self, movie_d):
        movie = self.get_one(movie_d["id"])
        if "title" in movie_d:
            movie.title = movie_d.get("title")
        if "description" in movie_d:
            movie.description = movie_d.get("description")
        if "trailer" in movie_d:
            movie.trailer = movie_d.get("trailer")
        if "year" in movie_d:
            movie.year = movie_d.get("year")
        if "rating" in movie_d:
            movie.rating = movie_d.get("rating")
        if "genre_id" in movie_d:
            movie.genre_id = movie_d.get("genre_id")
        if "director_id" in movie_d:
            movie.director_id = movie_d.get("director_id")
        self.dao.update(movie)

    def delete(self, rid):
        self.dao.delete(rid)











""" Homework 18 """
# class MovieService:
#     def __init__(self, dao: MovieDAO):
#         self.dao = dao
#
#     def get_one(self, mid):
#         return self.dao.get_one(mid)
#
#     def get_all(self, filters):
#         if filters.get("director_id"):
#             movies = self.dao.get_by_director_id(filters.get("director_id"))
#         elif filters.get("genre_id"):
#             movies = self.dao.get_by_genre_id(filters.get("genre_id"))
#         elif filters.get("year"):
#             movies = self.dao.get_by_year(filters.get("year"))
#         else:
#             movies = self.dao.get_all()
#         return movies
#
#
#
#     def create(self, data):
#         return self.dao.create(data)
#
#     def update(self, data):
#         mid = data.get("id")
#         movie = self.get_one(mid)
#
#         movie.title = data.get("title")
#         movie.description = data.get("description")
#         movie.trailer = data.get("trailer")
#         movie.year = data.get("year")
#         movie.rating = data.get("rating")
#         movie.genre_id = data.get("genre_id")
#         movie.director_id = data.get("director_id")
#
#         self.dao.update(movie)
#
#     def update_partial(self, data):
#         mid = data.get("id")
#         movie = self.get_one(mid)
#
#         if "title" in data:
#             movie.title = data.get("title")
#         if "description" in data:
#             movie.description = data.get("description")
#         if "trailer" in data:
#             movie.trailer = data.get("trailer")
#         if "year" in data:
#             movie.year = data.get("year")
#         if "rating" in data:
#             movie.rating = data.get("rating")
#         if "genre_id" in data:
#             movie.genre_id = data.get("genre_id")
#         if "director_id" in data:
#             movie.director_id = data.get("director_id")
#
#         self.dao.update(movie)
#
#     def delete(self, mid):
#         self.dao.delete(mid)