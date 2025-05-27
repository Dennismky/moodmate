from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.db.base import Base  

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    mood_logs = relationship("MoodLog", backref="user")
    suggestions = relationship("Suggestion", back_populates="user")

class MoodLog(Base):
    __tablename__ = 'mood_logs'

    id = Column(Integer, primary_key=True)
    mood = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
 suggestions-model

class Suggestion(Base):
    __tablename__ = 'suggestions'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    mood = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    user = relationship("User", back_populates="suggestions")

    
class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    mood = Column(String, nullable=False)
    text = Column(String, nullable=False)
usermodel-dennis
