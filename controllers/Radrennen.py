from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Radrennen


radrennen_blueprint = Blueprint('radrennen_blueprint', __name__)

@radrennen_blueprint.route("/Radrennen")
def radrennen():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Radrennen laden
    radrennen = session.query(Radrennen).all()
    print(radrennen)

    return render_template("radrennen.html")