from pydantic import BaseModel

class IsotopeResponse(BaseModel):
    id: int
    name: str
    symbol: str
    half_life_seconds: float

class DecayRequest(BaseModel):
    isotope_id: int
    initial_quantity: float
    elapsed_time: float

class DecayResponse(BaseModel):
    isotope_name: str
    initial_quantity: float
    remaining_quantity: float
    elapsed_time: float


    class Config:
        from_attributes = True