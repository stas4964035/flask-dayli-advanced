from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = TextAreaField('Текст записи', validators=[DataRequired()])
    picture = FileField('Изображение поста', validators=[FileAllowed([
        'jpg', 'png'])])
    submit = SubmitField('Сохранить')


class CommentForm(FlaskForm):
    comment = StringField('Комментарий', validators=[DataRequired()])
