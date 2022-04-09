#"""Sportler delete Form""""

from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators

class SportlerDeleteForm(FlaskForm):
    SportlerID = StringField("SportlerID",[validators.InputRequired()])