from dayli import create_app
from dayli import db

app = create_app()
app.app_context().push()
db.drop_all()
db.create_all()