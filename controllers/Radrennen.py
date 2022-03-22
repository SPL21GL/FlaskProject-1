from flask import request, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Radrennen
from forms.addRadrennenForm import AddRadrennenForm

radrennen_blueprint = Blueprint('radrennen_blueprint', __name__)

@radrennen_blueprint.route("/Radrennen")
def radrennen():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Radrennen laden
    radrennen = session.query(Radrennen).all()
    print(radrennen)

    return render_template("Radrennen/radrennen.html", radrennen=radrennen)

@radrennen_blueprint.route("/radrennen/add", methods=["GET", "POST"])
def radrennen_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    rennen = session.query(Radrennen).all()

    addRadrennenForm = AddRadrennenForm()

    if request.method == 'POST':

        if addRadrennenForm.validate_on_submit():
            rennen = Radrennen()
            rennen.Titel = addRadrennenForm.Titel.data
            rennen.Land = addRadrennenForm.Land.data
            rennen.Datum = addRadrennenForm.Datum.data
            rennen.LängeInKm = addRadrennenForm.LaengeInKm.data

            db.session.add(rennen)
            db.session.commit()

            return redirect("/Radrennen")

        else:
            raise "Fatal Error"
    else:
        return render_template("Radrennen/radrennenAdd.html", form=addRadrennenForm)
