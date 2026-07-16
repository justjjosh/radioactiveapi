from database import SessionLocal, engine, Base
from models import Isotope

print("Creating database tables...")

Base.metadata.create_all(bind=engine)
print("Seeding initial data... ")

#open a dedicated session to talk to the database
db = SessionLocal()

#python objects representing the isotopes we want to add to the database
Isotope_1 = Isotope(name="Cobalt-60", symbol="Co-60", half_life=166304808.0)  # in seconds
Isotope_2 = Isotope(name="Carbon-14", symbol="C-14", half_life=180874560000.0)
Isotope_3 = Isotope(name="Polonium-214", symbol="Po-214", half_life=0.0001643)

#staging and committing the new isotopes to the database
db.add_all([Isotope_1, Isotope_2, Isotope_3])
db.commit()

#close the session
db.close()
print("Database seeded successfully.")