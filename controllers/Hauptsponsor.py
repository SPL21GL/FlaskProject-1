from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db, Hauptsponsor
from forms.hauptsponsor.AddHauptsponsorForm import AddHauptsponsorForm
from forms.hauptsponsor.DeleteHauptsponsorForm import DeleteHauptsponsorForm


hauptsponsor_blueprint = Blueprint('hauptsponsor_blueprint', __name__)


@hauptsponsor_blueprint.route("/hauptsponsor")
def hauptsponsor():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    hauptsponsoren = session.query(Hauptsponsor).all()
    print(hauptsponsor)

    return render_template("hauptsponsor/hauptsponsor.html", hauptsponsoren=hauptsponsoren)


@hauptsponsor_blueprint.route("/hauptsponsor/add", methods=["GET", "POST"])
def add_hauptsponsor():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sponsor = session.query(Hauptsponsor).all()

    add_sponsor_form = AddHauptsponsorForm()

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
        return render_template("hauptsponsor/add_hauptsponsor.html", form=add_sponsor_form)


@hauptsponsor_blueprint.route("/hauptsponsor/delete", methods=["post"])
def delete_hauptsponsor():
    session:  sqlalchemy.orm.scoping.scoped_session = db.session
    delete_hauptsponsor_form = DeleteHauptsponsorForm()

    if delete_hauptsponsor_form.validate_on_submit():
        sponsor_to_delete = delete_hauptsponsor_form.SponsorID.data
        sponsorID_to_delete = db.session.query(Hauptsponsor).filter(
            Hauptsponsor.SponsorID == sponsor_to_delete)
        sponsorID_to_delete.delete()

        db.session.commit()

    else:
        flash("Fatal Error")

    return redirect("/hauptsponsor")


@hauptsponsor_blueprint.route("/hauptsponsor/edit", methods=["get", "post"])
def edit_hauptsponsor():
    session:  sqlalchemy.orm.scoping.scoped_session = db.session
    edit_hauptsponsor_form = AddHauptsponsorForm()

    sponsor_id = request.args["SponsorID"]
    hauptsponsor_to_edit = session.query(Hauptsponsor).filter(
        Hauptsponsor.SponsorID == sponsor_id).first()

    if request.method == "POST":
        if edit_hauptsponsor_form.validate_on_submit():
            hauptsponsor_to_edit = db.session.query(Hauptsponsor).filter(
                Hauptsponsor.SponsorID == sponsor_id).first()

            hauptsponsor_to_edit.SponsorID = edit_hauptsponsor_form.SponsorID.data
            hauptsponsor_to_edit.Name = edit_hauptsponsor_form.Name.data
            hauptsponsor_to_edit.Sponsorbetrag = edit_hauptsponsor_form.Sponsorbetrag.data
            hauptsponsor_to_edit.Werbungsart = edit_hauptsponsor_form.Werbungsart.data
            hauptsponsor_to_edit.Land = edit_hauptsponsor_form.Land.data

            db.session.commit()
        return redirect("/hauptsponsor")

    else:
        edit_hauptsponsor_form.SponsorID.data = hauptsponsor_to_edit.SponsorID
        edit_hauptsponsor_form.Name.data = hauptsponsor_to_edit.Name
        edit_hauptsponsor_form.Sponsorbetrag.data = hauptsponsor_to_edit.Sponsorbetrag
        edit_hauptsponsor_form.Werbungsart.data = hauptsponsor_to_edit.Werbungsart
        edit_hauptsponsor_form.Land.data = hauptsponsor_to_edit.Land

        return render_template("hauptsponsor/edit_hauptsponsor.html", form=edit_hauptsponsor_form)
