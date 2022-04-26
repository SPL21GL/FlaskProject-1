from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy, sqlalchemy.orm
from db.model import db, Sportler
from forms.sportler.AddSportlerForm import AddSportlerForm
from forms.sportler.DeleteSportlerForm import DeleteSportlerForm

sportler_blueprint = Blueprint('sportler_blueprint', __name__)


@sportler_blueprint.route("/sportler")
def sportler():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    # alle Sportler laden
    sportlers = session.query(Sportler).all()
    print(sportler)

    return render_template("sportler/sportler.html", sportlers=sportlers)


@sportler_blueprint.route("/sportler/add", methods=["GET", "POST"])
def add_sportler():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sportler = session.query(Sportler).all()

    add_sportler_form = AddSportlerForm()

    if request.method == 'POST':

        if add_sportler_form.validate_on_submit():
            sportler = Sportler()
            sportler.Vorname = add_sportler_form.Vorname.data
            sportler.Nachname = add_sportler_form.Nachname.data
            sportler.Land = add_sportler_form.Land.data
            sportler.Radmarke = add_sportler_form.Radmarke.data

            db.session.add(sportler)
            db.session.commit()

            return redirect("/sportler")

        else:
            return render_template("sportler/add_sportler.html", form=add_sportler_form)
    else:
        return render_template("sportler/add_sportler.html", form=add_sportler_form)


@sportler_blueprint.route("/sportler/delete", methods=["post"])
def delete_sportler():
    delete_sportler_form = DeleteSportlerForm()

    if delete_sportler_form.validate_on_submit():
        sportler_to_delete = delete_sportler_form.SportlerID.data
        sportlerID_to_delete = db.session.query(Sportler).filter(Sportler.SportlerID == sportler_to_delete)
        sportlerID_to_delete.delete()

        flash(f"Sportler with id {sportlerID_to_delete} has been deleted")
        db.session.commit()
    else:
        flash("Fatal Error")

    return redirect("/sportler")


@sportler_blueprint.route("/sportler/edit", methods=["get","post"])
def edit_sportler():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    edit_sportler_form = AddSportlerForm()

    sportler = request.args["SportlerID"]
    sportler_to_edit = session.query(Sportler).filter(Sportler.SportlerID == sportler).first()
    
    if request.method == "POST":
        if edit_sportler_form.validate_on_submit():
            sportler_to_edit = db.session.query(Sportler).filter(Sportler.SportlerID == sportler).first()
            
            sportler_to_edit.SportlerID = edit_sportler_form.SportlerID.data
            sportler_to_edit.Land = edit_sportler_form.Land.data
            sportler_to_edit.Vorname = edit_sportler_form.Vorname.data
            sportler_to_edit.Nachname = edit_sportler_form.Nachname.data
            sportler_to_edit.Radmarke = edit_sportler_form.Radmarke.data
            
            db.session.commit()
        return redirect("/sportler")
    
    else:
        edit_sportler_form.SportlerID.data = sportler_to_edit.SportlerID
        edit_sportler_form.Land.data = sportler_to_edit.Land
        edit_sportler_form.Vorname.data = sportler_to_edit.Vorname
        edit_sportler_form.Nachname.data = sportler_to_edit.Nachname
        edit_sportler_form.Radmarke.data = sportler_to_edit.Radmarke
        
        return render_template("sportler/edit_sportler.html", form = edit_sportler_form)

