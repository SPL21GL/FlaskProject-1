from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Hauptsponsor


hauptsponsor_blueprint = Blueprint('hauptsponsor_blueprint', __name__)

@hauptsponsor_blueprint.route("/hauptsponsor")
def hauptsponsor():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Hauptsponsoren laden
    hauptsponsor = session.query(Hauptsponsor).all()
    print(hauptsponsor)

    return render_template("hauptsponsor.html")