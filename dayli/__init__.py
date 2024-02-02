from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_loginmanager import LoginManager
from dayli.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from dayli.main.routes import main
    app.register_blueprint(main)
    return app


db = SQLAlchemy()
login_manager = LoginManager()
