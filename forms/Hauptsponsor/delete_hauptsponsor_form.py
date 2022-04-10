from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class Delete_hauptsponsor_form(FlaskForm):
    SponsorID = StringField("SponsorID",[validators.InputRequired()])