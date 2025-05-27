from models import  MoodLog,engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, timezone
from lib.db.create import engine, Base
from lib.db.models import Suggestion, User


import random

Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data to avoid duplicates
session.query(MoodLog).delete()
session.query(Suggestion).delete()
session.query(User).delete()
session.commit()

# Create users
users = [
    User(name="Christina"),
    User(name="James"),
    User(name="Aisha"),
]
session.add_all(users)
session.commit()

# List of moods
moods = [
    "Happy", "Sad", "Excited", "Anxious", "Calm",
    "Energetic", "Tired", "Frustrated", "Hopeful", "Content",
    "Nervous", "Relaxed", "Overwhelmed", "Inspired", "Lonely",
    "Grateful", "Bored", "Confident", "Restless", "Curious"
]

# Current time in UTC
now = datetime.now(timezone.utc)

# Generating 30 random mood logs
mood_logs = []
for _ in range(30):
    mood = random.choice(moods)
    user = random.choice(users)
    # Random timestamp within last 10 days
    timestamp = now - timedelta(days=random.randint(0, 9),
                                hours=random.randint(0, 23),
                                minutes=random.randint(0, 59))
    mood_logs.append(MoodLog(mood=mood, timestamp=timestamp, user_id=user.id))

session.add_all(mood_logs)
session.commit()

print("Database seeded with 3 users and 30 mood logs!")

# Seed suggestions in the database
def seed_suggestions():
    suggestions_data = [
        {"text": "Take a deep breath and relax.", "mood": "stressed"},
        {"text": "Go for a short walk outside.", "mood": "sad"},
        {"text": "Try writing down three things you're grateful for.", "mood": "neutral"},
        {"text": "Call a friend or family member.", "mood": "lonely"},
        {"text": "Listen to your favorite upbeat music.", "mood": "happy"},
    ]

    for s in suggestions_data:
        suggestion = Suggestion(text=s["text"], mood=s["mood"])
        session.add(suggestion)

    session.commit()
    print("Seeded suggestions table with default data.")

if __name__ == "__main__":
    seed_suggestions()
