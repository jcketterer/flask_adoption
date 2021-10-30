from flask import (
    Flask,
    request,
    render_template,
    redirect,
    flash,
    session,
    jsonify,
    url_for,
)
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_new_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add_new_pet.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data

        db.session.commit()
        flash(f"{pet.name} updated")

        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)


@app.route("/api/pets/<int:id>", methods=["GET"])
def api_get_pet(id):

    pet = Pet.query.get_or_404(id)

    info = {"name": pet.name, "age": pet.age, "url": pet.photo_url}

    return jsonify(info)
