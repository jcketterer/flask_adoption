from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

poppy = Pet(
    name="Poppy",
    species="Dog",
    photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPnwNnkeQBS9cqac82GWWG9AQpsU0wVmSU-Q&usqp=CAU",
    age=2,
)
arthur = Pet(
    name="Arthur",
    species="Dog",
    photo_url="https://www.chichisandme.com/wp-content/uploads/2019/08/pure-white-chihuahua-source-instagram-.jpg",
    age=14,
)
jasper = Pet(
    name="Jasper",
    species="Porcupine",
    photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcCHN3WjqZTjjV2yj2qVZFhfPkGaEY2FjIKg&usqp=CAU",
    age=2,
)

dr_claw = Pet(name="Dr.Claw", species="Cat")


db.session.add_all([poppy, arthur, jasper, dr_claw])
db.session.commit()
