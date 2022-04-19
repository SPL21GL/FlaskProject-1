from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField
from wtforms import validators

class Add_hauptsponsor_form(FlaskForm):
    SponsorID = StringField("SponsorID")
    Name = StringField("Name")
    Sponsorbetrag = DecimalField("Sponsorbetrag")
    Werbungsart = StringField("Land")
    Land = StringField("Radmarke")
