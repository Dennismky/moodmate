
from sqlalchemy import create_engine,inspect
from lib.db.base import Base
from lib.db.models import User, MoodLog, Suggestion, Quote  

engine = create_engine('sqlite:///lib/db/moodmate.db')

print("Known tables:", Base.metadata.tables.keys()) 

Base.metadata.create_all(engine)

print("Database and all tables created successfully!")