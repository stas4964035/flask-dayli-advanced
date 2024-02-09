from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dayli.models import User, Post
from dayli import db
from dayli import create_app

app = create_app()
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))