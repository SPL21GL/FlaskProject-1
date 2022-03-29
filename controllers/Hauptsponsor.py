from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from db.model import db,Hauptsponsor
from forms.addSponsorForm import AddSponsorForm
from forms.SponsorDelete import SponsorDeleteForm
hauptsponsor_blueprint = Blueprint('hauptsponsor_blueprint', __name__)

@hauptsponsor_blueprint.route("/Hauptsponsor")
def hauptsponsor():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle Hauptsponsoren laden
    hauptsponsor = session.query(Hauptsponsor).all()
    print(hauptsponsor)

    return render_template("Hauptsponsor/hauptsponsor.html", hauptsponsor = hauptsponsor)

@hauptsponsor_blueprint.route("/sponsor/add", methods=["GET", "POST"])
def Hauptsponsor_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sponsor = session.query(Hauptsponsor).all()

    addSponsorForm = AddSponsorForm()

    if request.method == 'POST':

        if addSponsorForm.validate_on_submit():
            sponsor = Hauptsponsor()
            sponsor.Name = addSponsorForm.Name.data
            sponsor.Sponsorbetrag = addSponsorForm.Sponsorbetrag.data
            sponsor.Land = addSponsorForm.Land.data
            sponsor.Werbungsart = addSponsorForm.Werbungsart.data

            db.session.add(sponsor)
            db.session.commit()

            return redirect("/Hauptsponsor")

        else:
            raise "Fatal Error"
    else:
        return render_template("Hauptsponsor/hauptsponsorAdd.html", form=addSponsorForm)

@hauptsponsor_blueprint.route("/products/delete", methods=["post"])
def deleteProduct():

    deleteSponsorForm = SponsorDeleteForm()

    if deleteSponsorForm.validate_on_submit():

        SponsorToDelete = deleteSponsorForm.productCode.data
        NameToDelete = db.session.query(Hauptsponsor).filter(Hauptsponsor.Name == SponsorToDelete)
        NameToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Product with id {NameToDelete} has been deleted")    

    return redirect("/Hauptsponsor")