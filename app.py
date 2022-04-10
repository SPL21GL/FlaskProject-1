#"""main""""
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from controllers.index import index_blueprint
from controllers.radrennen import radrennen_blueprint
from controllers.sportler import sportler_blueprint
from controllers.hauptsponsor import hauptsponsor_blueprint
from db.model import db

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Sportverein"

db.init_app(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(hauptsponsor_blueprint)
app.register_blueprint(sportler_blueprint)
app.register_blueprint(radrennen_blueprint)

app.run(debug=True)
