# lib/db/base.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database path (make sure this path matches your actual DB file)
engine = create_engine("sqlite:///lib/db/moodmate.db", echo=True)

# Create a configured "Session" class and an instance
Session = sessionmaker(bind=engine)
session = Session()

# Base class for models
Base = declarative_base()
