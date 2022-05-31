from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm
from db.model import db, Radrennen
from forms.radrennen.AddRadrennenForm import AddRadrennenForm
from forms.radrennen.DeleteRadrennenForm import DeleteRadrennenForm


radrennen_blueprint = Blueprint('radrennen_blueprint', __name__)


@radrennen_blueprint.route("/radrennen")
def radrennen():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    radrennen = session.query(Radrennen).all()
    print(radrennen)

    return render_template("radrennen/radrennen.html", radrennen=radrennen)


@radrennen_blueprint.route("/radrennen/add", methods=["GET", "POST"])
def add_radrennen():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    rennen = session.query(Radrennen).all()

    add_radrennen_form = AddRadrennenForm()

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
            return render_template("radrennen/add_radrennen.html", form=add_radrennen_form)
    else:
        return render_template("radrennen/add_radrennen.html", form=add_radrennen_form)


@radrennen_blueprint.route("/radrennen/delete", methods=["post"])
def delete_radrennen():
    delete_radrennen_form = DeleteRadrennenForm()

    if delete_radrennen_form.validate_on_submit():
        radrennen_to_delete = delete_radrennen_form.RadrennenID.data
        RadrennenID_to_delete = db.session.query(Radrennen).filter(
            Radrennen.RadrennenID == radrennen_to_delete)
        RadrennenID_to_delete.delete()

        db.session.commit()
    else:
        flash("Fatal Error")

    return redirect("/radrennen")


@radrennen_blueprint.route("/radrennen/edit", methods=["get", "post"])
def edit_radrennen():
    session:  sqlalchemy.orm.scoping.scoped_session = db.session

    edit_radrennen_form = AddRadrennenForm()

    radrennen_id = request.args["RadrennenID"]
    radrennen_to_edit = session.query(Radrennen).filter(
        Radrennen.RadrennenID == radrennen_id).first()

    if request.method == "POST":
        if edit_radrennen_form.validate_on_submit():
            radrennen_to_edit = db.session.query(Radrennen).filter(
                Radrennen.RadrennenID == radrennen_id).first()

            radrennen_to_edit.RadrennenID = edit_radrennen_form.RadrennenID.data
            radrennen_to_edit.Land = edit_radrennen_form.Land.data
            radrennen_to_edit.Titel = edit_radrennen_form.Titel.data
            radrennen_to_edit.Datum = edit_radrennen_form.Datum.data
            radrennen_to_edit.LaengeInKm = edit_radrennen_form.LaengeInKm.data

            db.session.commit()
        return redirect("/radrennen")

    else:
        edit_radrennen_form.RadrennenID.data = radrennen_to_edit.RadrennenID
        edit_radrennen_form.Land.data = radrennen_to_edit.Land
        edit_radrennen_form.Titel.data = radrennen_to_edit.Titel
        edit_radrennen_form.Datum.data = radrennen_to_edit.Datum
        edit_radrennen_form.LaengeInKm.data = radrennen_to_edit.LaengeInKm

        return render_template("radrennen/edit_radrennen.html", form=edit_radrennen_form)
