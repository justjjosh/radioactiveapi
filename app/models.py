from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class Isotope(Base):
    __tablename__ = "radioactive_elements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    symbol = Column(String, unique=True, index=True, nullable=False)
    half_life = Column(Float, nullable=False)  # Half-life in seconds