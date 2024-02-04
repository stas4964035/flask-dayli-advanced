from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = TextAreaField('Текст записи', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class CommentForm(FlaskForm):
    comment = StringField('Комментарий', validators=[DataRequired()])
