# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api

from config import Config

from setup_db import db
from views.genre import genre_ns
from views.dirctor import director_ns
from views.movie import movie_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)

    # create_data(app, db)


# функция создания БД ( на случай если нет БД)
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         #         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(#здесь список созданных объектов)

app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
