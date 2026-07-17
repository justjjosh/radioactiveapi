from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Isotope
from app.schemas import IsotopeResponse

app = FastAPI()

@app.get ("/")
def root():
    return {"message": "Radioactive API is running!"}

@app.get("/isotopes", response_model=list[IsotopeResponse])
def list_isotopes(db: Session = Depends(get_db)):
     return db.query(Isotope).all()

@app.get("/isotopes/{isotope_id}", response_model=IsotopeResponse)
def get_isotope(isotope_id: int, db: Session = Depends(get_db)):
    isotope = db.query(Isotope).filter(Isotope.id == isotope_id).first()
    if isotope is None:
        raise HTTPException(status_code=404, detail="Isotope not found")
    return isotope

    