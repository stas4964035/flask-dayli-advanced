from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dayli.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from dayli.main.routes import main
    app.register_blueprint(main)

    from dayli.users.routes import users
    app.register_blueprint(users)

    from dayli.posts.routes import posts
    app.register_blueprint(posts)

    from dayli.errors.handlers import errors
    app.register_blueprint(errors)

    return app
