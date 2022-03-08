from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from controllers.index import index_blueprint


from db.model import db

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Sportverein"
db.init_app(app)


app.register_blueprint(index_blueprint)

app.run(debug=True)