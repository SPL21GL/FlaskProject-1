from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db
from db.model import Radrennen

index_blueprint = Blueprint('index_blueprint', __name__)

@index_blueprint.route("/")
def index():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Sportler laden
    radrennen = session.query(Radrennen).all()
    print(radrennen)

    return render_template("index.html")