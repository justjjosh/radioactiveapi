from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Isotope
from app.schemas import IsotopeResponse, DecayRequest, DecayResponse
from app.physics import quantity_remaining, decay_curve_points


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

@app.post("/decay", response_model=DecayResponse)
def calculate_decay( request: DecayRequest, db: Session = Depends(get_db)):
    isotope = db.query(Isotope).filter(Isotope.id == request.isotope_id).first()
    if isotope is None:
        raise HTTPException(status_code=404, detail="Isotope not found")
    
    remaining_quantity = quantity_remaining(
        request.initial_quantity,
        isotope.half_life_seconds,
        request.elapsed_time_seconds
    )
    
    return DecayResponse(
        isotope_name=isotope.name,
        initial_quantity=request.initial_quantity,
        remaining_quantity=remaining_quantity,
        elapsed_time_seconds=request.elapsed_time_seconds
    )

@app.get("/isotopes/{isotope_id}/decay-curve")
def get_decay_curve(isotope_id: int, initial_quantity: float, duration_seconds: float, n_points: int = 100, db: Session = Depends(get_db)):
    isotope = db.query(Isotope).filter(Isotope.id == isotope_id).first()
    if isotope is None:
        raise HTTPException(status_code=404, detail="Isotope not found")
    
    time_points, value_points = decay_curve_points(
        initial_quantity,
        isotope.half_life_seconds,
        duration_seconds,
        n_points
    )
    
    return {
        "isotope": isotope.name,
        "time_points": time_points.tolist(), 
        "remaining_quantities": value_points.tolist()
         }
    