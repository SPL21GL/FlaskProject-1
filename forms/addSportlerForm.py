from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators

class AddSportlerForm(FlaskForm):
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Land = StringField("Land")
    Radmarke = StringField("Radmarke")
