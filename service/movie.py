from dao.model.models import Movie
from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by_many(self, **kwargs):
        return self.movie_dao.get_movies_by_many(**kwargs)

    def add_film(self, data) -> None:
        self.movie_dao.create_movie(**data)

    def update_film(self, data) -> None:
        self.movie_dao.update_movie(data)

    def delete_film_by_id(self, id) -> None:
        self.movie_dao.delete(id)
