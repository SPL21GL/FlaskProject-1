from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class DeleteHauptsponsorForm(FlaskForm):
    SponsorID = StringField("SponsorID", [validators.InputRequired()])
