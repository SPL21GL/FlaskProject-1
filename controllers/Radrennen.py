from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Radrennen
from forms.Radrennen.add_radrennen_form import Add_radrennen_form
from forms.Radrennen.delete_radrennen_form import Delete_radrennen_form


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
            rennen.LaengeInKm = add_radrennen_form.LaengeInKm.data

            db.session.add(rennen)
            db.session.commit()

            return redirect("/radrennen")

        else:
            raise "Fatal Error"
    else:
        return render_template("radrennen/add_radrennen.html", form=add_radrennen_form)


@radrennen_blueprint.route("/radrennen/delete", methods=["post"])
def delete_radrennen():
    delete_radrennen_form = Delete_radrennen_form()

    if delete_radrennen_form.validate_on_submit():
        radrennen_to_delete = delete_radrennen_form.RadrennenID.data
        RadrennenID_to_delete = db.session.query(Radrennen).filter(Radrennen.RadrennenID == radrennen_to_delete)
        RadrennenID_to_delete.delete()

        flash(f"Radrennen with id {{RadrennenID_to_delete}} has been deleted")
        db.session.commit()
    else:
        flash("Fatal Error")

    return redirect("/radrennen")


@radrennen_blueprint.route("radrennen/edit", methods=["get","post"])
def edit_radrennen():
    sessiton :  sqlalchemy.orm.scoping.scoped_session = db.session

    #edit_radrennen_form =
