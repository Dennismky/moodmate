import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to the database file
db_path = os.path.join(BASE_DIR, "moodmate.db")

# Create SQLite engine with absolute path
engine = create_engine(f"sqlite:///lib/db/moodmate.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
