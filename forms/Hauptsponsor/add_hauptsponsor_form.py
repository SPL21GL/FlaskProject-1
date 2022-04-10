from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField


class Add_sponsor_form(FlaskForm):
    Name = StringField("Name")
    Sponsorbetrag = DecimalField("Sponsorbetrag")
    Werbungsart = StringField("Land")
    Land = StringField("Radmarke")
