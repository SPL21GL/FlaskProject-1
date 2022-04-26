from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class DeleteRadrennenForm(FlaskForm):
    RadrennenID = StringField("RadrennenID",[validators.InputRequired()])