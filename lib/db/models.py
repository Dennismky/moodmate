from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base 

# ---------------------
# User Model
# ---------------------
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    mood_logs = relationship('MoodLog', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

# ---------------------
# MoodLog Model
# ---------------------
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

