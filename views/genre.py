from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')


@genre_ns.route('/')
@genre_ns.param("director_id")
@genre_ns.param("genre_id")
@genre_ns.param("year")
class GenresView(Resource):
    def get(self):
        """Получение всех жанров"""

        # метод который, достанет из БД все сущности
        return "", 200

    def post(self):
        """Добавление нового жанра"""

        # Метод который, добавит новую запись в БД
        return "", 201

@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        """Получение жанра по id"""

        # метод который, достанет из БД все сущности по id
        return "", 200

    def put(self, genre_id: int):
        """Изменение информации о жанре"""

        # Метод который, изменит новую запись в БД
        return "", 201

    def delete(self, genre_id: int):
        """Удаление жанра"""

        # Метод который, удалит запись в БД
        return "", 201