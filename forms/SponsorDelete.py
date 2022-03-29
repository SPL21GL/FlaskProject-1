from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators

class SponsorDeleteForm(FlaskForm):
    Name = StringField("Name",[validators.InputRequired()])