from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class Edit_sportler_form(FlaskForm):
    SportlerID = StringField("SportlerID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Land = StringField("Land")
    Radmarke = StringField("Radmarke")