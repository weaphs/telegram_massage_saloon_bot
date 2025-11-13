#db/models.py
from sqlalchemy import Column, Integer, String, Date, Time, Boolean, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String)
    book_date = Column(Date)  # YYYY-MM-DD
    book_time = Column(Time) # HH:MM:SS
    status = Column(String, default="free")  # free, booked
