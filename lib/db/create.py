

from lib.db.base import Base
from lib.db.models import User, MoodLog, Suggestion
from sqlalchemy import create_engine
from models import Base, engine, Quote


engine = create_engine('sqlite:///lib/db/moodmate.db')
Base.metadata.create_all(engine)

print("Database and all tables created successfully!")
