from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    summary = StringField('Quick Summary', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Blog picture', validators=[FileAllowed(['jpg', 'png'])])
    category = SelectField(u'Category',
                           choices=[('tech', 'Technology'), ('health', 'Health'), ('environment', 'Environment'), ('ent', 'Entertainment')]
                           , validators=[DataRequired()])
    submit = SubmitField('Post')