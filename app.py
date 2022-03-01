from flask import Flask, redirect, request, flash, session
from flask.templating import render_template

from db.model import db

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Sportverein"
db.init_app(app)


#app routes

app.run(debug=True)