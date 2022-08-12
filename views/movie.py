from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
@movie_ns.param("director_id")
@movie_ns.param("genre_id")
@movie_ns.param("year")
class MoviesView(Resource):
    def get(self):
        """Получение всех фильмов"""

        # метод который, достанет из БД все сущности
        return "", 200

    def post(self):
        """Добавление нового фильма"""

        # Метод который, который добавит новую запись в БД
        return "", 201

@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """Получение фильма по id"""

        # метод который, достанет из БД все сущности по id
        return "", 200

    def put(self, movie_id: int):
        """Изменение информации о фильме по id"""

        # Метод который, изменит новую запись в БД
        return "", 201

    def delete(self, movie_id: int):
        """Удаление фильма по id"""

        # Метод который, удалит запись в БД
        return "", 201