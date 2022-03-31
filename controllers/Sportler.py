from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db, Sportler
from forms.addSportlerForm import AddSportlerForm
from forms.sportler_delete import SportlerDeleteForm
sportler_blueprint = Blueprint('sportler_blueprint', __name__)


@sportler_blueprint.route("/Sportler")
def sportler():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    # alle Sportler laden
    sportlers = session.query(Sportler).all()
    print(sportler)

    return render_template("Sportler/sportler.html", sportlers=sportlers)


@sportler_blueprint.route("/sportler/add", methods=["GET", "POST"])
def sportler_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sportler = session.query(Sportler).all()

    addSportlerForm = AddSportlerForm()

    if request.method == 'POST':

        if addSportlerForm.validate_on_submit():
            sportler = Sportler()
            sportler.Vorname = addSportlerForm.Vorname.data
            sportler.Nachname = addSportlerForm.Nachname.data
            sportler.Land = addSportlerForm.Land.data
            sportler.Radmarke = addSportlerForm.Radmarke.data

            db.session.add(sportler)
            db.session.commit()

            return redirect("/Sportler")

        else:
            raise "Fatal Error"
    else:
        return render_template("Sportler/sportlerAdd.html", form=addSportlerForm)


@sportler_blueprint.route("/sportler/delete", methods=["post"])
def delete_sportler():
    #"""delete Sportler function""""

    deleteSportlerForm = SportlerDeleteForm()

    if deleteSportlerForm.validate_on_submit():

        sportlerToDelete = deleteSportlerForm.SportlerID.data
        NameToDelete = db.session.query(Sportler).filter(
            Sportler.SportlerID == sportlerToDelete)
        NameToDelete.delete()

        flash(f"Sponsor with id {NameToDelete} has been deleted")
        db.session.commit()
    else:
        flash("Fatal Error")

    return redirect("/Sportler")
