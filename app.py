from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from controllers.index import index_blueprint
from controllers.Radrennen import radrennen_blueprint
from controllers.Sportler import sportler_blueprint
from controllers.Hauptsponsor import hauptsponsor_blueprint
from db.model import db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Sportverein"

csrf = CSRFProtect(app)

db.init_app(app)


app.register_blueprint(index_blueprint)
app.register_blueprint(hauptsponsor_blueprint)
app.register_blueprint(sportler_blueprint)
app.register_blueprint(radrennen_blueprint)

app.run(debug=True)