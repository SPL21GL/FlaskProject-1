from flask import Flask,request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Sportler
from forms.addSportlerForm import AddSportlerForm
sportler_blueprint = Blueprint('sportler_blueprint', __name__)

@sportler_blueprint.route("/Sportler")
def sportler():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Sportler laden
    sportler = session.query(Sportler).all()
    print(sportler)

    return render_template("sportler.html")

@sportler_blueprint.route("/sportler/add", methods=["GET","POST"])
def products_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    sportler = session.query(Sportler).all()
    
    addSportlerForm = AddSportlerForm()

    if request.method == 'POST':
        
        if addSportlerForm.validate_on_submit():
            print("gültig")
            return render_template("sportler_add.html", form = addSportlerForm)
        else:
            raise "Fatal Error"
    else:
        return render_template("sportler_add.html",form = addSportlerForm)