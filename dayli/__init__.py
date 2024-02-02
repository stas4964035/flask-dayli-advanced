from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dayli.config import Config
from flask_bcrypt import Bcrypt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)

    from dayli.main.routes import main
    app.register_blueprint(main)
    return app


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
