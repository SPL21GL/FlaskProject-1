from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class Add_sportler_form(FlaskForm):
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Land = StringField("Land")
    Radmarke = StringField("Radmarke")
