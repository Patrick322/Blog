from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    description = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')