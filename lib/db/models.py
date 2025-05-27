from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

engine = create_engine('sqlite:///moodmate.db') 

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    mood_logs = relationship("MoodLog", backref="user")

class MoodLog(Base):
    __tablename__ = 'mood_logs'

    id = Column(Integer, primary_key=True)
    mood = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    
class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    mood = Column(String, nullable=False)
    text = Column(String, nullable=False)
