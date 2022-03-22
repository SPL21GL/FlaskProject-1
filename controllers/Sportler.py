from flask import Flask, request, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db, Sportler
from forms.addSportlerForm import AddSportlerForm

sportler_blueprint = Blueprint('sportler_blueprint', __name__)


@sportler_blueprint.route("/Sportler")
def sportler():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    # alle Sportler laden
    sportlers = session.query(Sportler).all()
    print(sportler)

    return render_template("sportler.html", sportlers = sportlers)


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
        return render_template("sportlerAdd.html", form=addSportlerForm)
