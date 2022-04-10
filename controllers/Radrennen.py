from flask import request, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Radrennen
from forms.Radrennen.add_radrennen_form import Add_radrennen_form


radrennen_blueprint = Blueprint('radrennen_blueprint', __name__)


@radrennen_blueprint.route("/radrennen")
def radrennen():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Radrennen laden
    radrennen = session.query(Radrennen).all()
    print(radrennen)

    return render_template("radrennen/radrennen.html", radrennen=radrennen)


@radrennen_blueprint.route("/radrennen/add", methods=["GET", "POST"])
def add_radrennen():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    rennen = session.query(Radrennen).all()

    add_radrennen_form = Add_radrennen_form()

    if request.method == 'POST':
        if add_radrennen_form.validate_on_submit():
            rennen = Radrennen()
            rennen.Titel = add_radrennen_form.Titel.data
            rennen.Land = add_radrennen_form.Land.data
            rennen.Datum = add_radrennen_form.Datum.data
            rennen.LaengeInKM = add_radrennen_form.LaengeInKM.data

            db.session.add(rennen)
            db.session.commit()

            return redirect("/radrennen")

        else:
            raise "Fatal Error"
    else:
        return render_template("radrennen/add_radrennen.html", form=add_radrennen_form)
