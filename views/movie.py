from flask import request
from flask_restx import Resource, Namespace

from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Получение всех фильмов"""

        # метод, который достанет из БД все сущности

        if len(request.args) > 0:
            return movies_schema.dump(movie_service.get_movie_by_many(**request.args)), 200
        else:
            return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        """Добавление нового фильма"""

        # Метод, который добавит новую запись в БД

        movie_service.add_film(request.json)
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """Получение фильма по id"""

        # метод, который достанет из БД все сущности по id
        if len(request.args):
            return movies_schema.dump(movie_service.get_movie_by_many(request.args)), 200

        else:
            return movies_schema.dump(movie_service.get_movies()), 200

    def put(self, movie_id: int):
        """Изменение информации о фильме по id"""

        # Метод, который изменит новую запись в БД

        movie_service.update_film(request.json)
        return "", 201

    def delete(self, movie_id: int):
        """Удаление фильма по id"""

        # Метод, который удалит запись в БД

        movie_service.delete_film_by_id(movie_id)
        return "", 201
