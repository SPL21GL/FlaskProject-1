from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class Delete_radrennen_form(FlaskForm):
    RadrennenID = StringField("RadrennenID",[validators.InputRequired()])