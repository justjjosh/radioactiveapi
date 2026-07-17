from app.database import SessionLocal, engine, Base
from app.models import Isotope

def seed_database():
    Base.metadata.create_all(bind=engine) #create tables if they don't exist
    db = SessionLocal() #open a dedicated session to talk to the database

    isotopes = [
        Isotope(name="Cobalt-60", symbol="Co-60", half_life_seconds=166304808.0),
        Isotope(name="Carbon-14", symbol="C-14", half_life_seconds=180874560000.0),
        Isotope(name="Polonium-214", symbol="Po-214", half_life_seconds=0.0001643)
    ]
    db.add_all(isotopes)
    db.commit()
    db.close()
    print(f"Seeded {len(isotopes)} isotopes into the database.")

if __name__ == "__main__":
    seed_database()