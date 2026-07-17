from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base

class Isotope(Base):
    __tablename__ = "radioactive_isotopes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    symbol = Column(String, unique=True, index=True, nullable=False)
    half_life_seconds = Column(Float, nullable=False)  # Half-life in seconds