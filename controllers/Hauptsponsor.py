from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Hauptsponsor
from forms.Hauptsponsor.add_hauptsponsor_form import Add_sponsor_form
from forms.Hauptsponsor.delete_hauptsponsor_form import Delete_hauptsponsor_form


hauptsponsor_blueprint = Blueprint('hauptsponsor_blueprint', __name__)


@hauptsponsor_blueprint.route("/hauptsponsor")
def hauptsponsor():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Hauptsponsoren laden
    hauptsponsoren = session.query(Hauptsponsor).all()
    print(hauptsponsor)

    return render_template("hauptsponsor/hauptsponsor.html", hauptsponsoren = hauptsponsoren)


@hauptsponsor_blueprint.route("/hauptsponsor/add", methods=["GET", "POST"])
def add_hauptsponsor():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sponsor = session.query(Hauptsponsor).all()
    add_sponsor_form = Add_sponsor_form()

    if request.method == 'POST':
        if add_sponsor_form.validate_on_submit():
            sponsor = Hauptsponsor()
            sponsor.Name = add_sponsor_form.Name.data
            sponsor.Sponsorbetrag = add_sponsor_form.Sponsorbetrag.data
            sponsor.Land = add_sponsor_form.Land.data
            sponsor.Werbungsart = add_sponsor_form.Werbungsart.data

            db.session.add(sponsor)
            db.session.commit()

            return redirect("/hauptsponsor")

        else:
            raise "Fatal Error"
    else:
        return render_template("hauptsponsor/add_hauptsponsor.html", form=add_sponsor_form)


@hauptsponsor_blueprint.route("/hauptsponsor/delete", methods=["post"])
def delete_hauptsponsor():
    delete_hauptsponsor_form = Delete_hauptsponsor_form()

    if delete_hauptsponsor_form.validate_on_submit():
        sponsor_to_delete = delete_hauptsponsor_form.SponsorID.data
        sponsorID_to_delete = db.session.query(Hauptsponsor).filter(Hauptsponsor.SponsorID == sponsor_to_delete)
        sponsorID_to_delete.delete()
        
        flash(f"Sponsor with id {sponsorID_to_delete} has been deleted")    
        db.session.commit()

    else:
        flash("Fatal Error")

    return redirect("/hauptsponsor")


    