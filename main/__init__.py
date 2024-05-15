from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_pyfile('config.py')
    # JWTManager(app)
    db.init_app(app)

    from main.route import route

    app.register_blueprint(route)

    return app
