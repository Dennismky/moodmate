from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from lib.db.base import Base  


# User Model

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    mood_logs = relationship("MoodLog", back_populates="user")
    suggestions = relationship("Suggestion", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"



# MoodLog Model

class MoodLog(Base):
    __tablename__ = 'mood_logs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    mood = Column(String, nullable=False)
    suggestion = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='mood_logs')

    def __repr__(self):
        return f"<MoodLog(id={self.id}, mood='{self.mood}', timestamp='{self.timestamp}')>"



# Suggestion Model

class Suggestion(Base):
    __tablename__ = 'suggestions'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    mood = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    user = relationship("User", back_populates="suggestions")

    def __repr__(self):
        return f"<Suggestion(id={self.id}, text='{self.text}')>"



# Quote Model

class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    mood = Column(String, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f"<Quote(id={self.id}, mood='{self.mood}', text='{self.text}')>"
