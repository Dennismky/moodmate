from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    mood_logs = relationship("MoodLog", back_populates="user")
    suggestions = relationship("Suggestion", back_populates="user")

