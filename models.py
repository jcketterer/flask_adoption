from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


GENERIC_IMAGE = (
    "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"
)


class Pet(db.Model):
    """Pet Database"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def img_url(self):
        """Displays an image for pet available or not"""

        return self.photo_url or GENERIC_IMAGE
