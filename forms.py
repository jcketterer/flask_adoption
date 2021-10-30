from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    TextAreaField,
    RadioField,
    SelectField,
)
from wtforms.validators import InputRequired, NumberRange, Email, Optional, URL, Length


class AddPetForm(FlaskForm):
    pet_name = StringField(
        "Pet Name", validators=[InputRequired(message="Please enter a pet name")]
    )
    species = SelectField(
        "Species?",
        choices=[
            ("cat", "Cat"),
            ("dog", "Dog"),
            ("porcupine", "Porcupine"),
        ],
    )
    photo_url = StringField("Enter Image URL", validators=[Optional(), URL()])

    age = IntegerField(
        "Please enter age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )
    notes = TextAreaField("Notes: ", validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes: ", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
