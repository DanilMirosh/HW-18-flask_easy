from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
@director_ns.param("director_id")
@director_ns.param("genre_id")
@director_ns.param("year")
class DirectorsView(Resource):
    def get(self):
        """Получение всех режиссеров"""

        # метод который, достанет из БД все сущности
        return "", 200

    def post(self):
        """Добавление нового режиссера"""

        # Метод который, добавит новую запись в БД
        return "", 201

@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        """Получение режиссера по id"""

        # метод который, достанет из БД все сущности по id
        return "", 200

    def put(self, director_id: int):
        """Изменение информации о режиссере"""

        # Метод который, изменит новую запись в БД
        return "", 201

    def delete(self, director_id: int):
        """Удаление режиссера"""

        # Метод который, удалит запись в БД
        return "", 201