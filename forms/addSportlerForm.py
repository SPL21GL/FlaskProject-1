from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class AddSportlerForm(FlaskForm):
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Land = StringField("Land")
    Radmarke = StringField("Radmarke")
