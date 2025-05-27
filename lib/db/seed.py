from models import User, MoodLog, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random

Session = sessionmaker(bind=engine)
session = Session()

# clearing existing data
session.query(MoodLog).delete()
session.query(User).delete()
session.commit()

# Creating users
users = [
    User(name="Christina"),
    User(name="James"),
    User(name="Aisha"),
]
session.add_all(users)
session.commit()

# Listing of moods
moods = [
    "Happy", "Sad", "Excited", "Anxious", "Calm",
    "Energetic", "Tired", "Frustrated", "Hopeful", "Content",
    "Nervous", "Relaxed", "Overwhelmed", "Inspired", "Lonely",
    "Grateful", "Bored", "Confident", "Restless", "Curious"
]

# Creating at  mood logs randomly distributed
mood_logs = []

# now = datetime.utcnow()

from datetime import datetime, timezone
now = datetime.now(timezone.utc)

for i in range(30):  # 30 logs total for more variety
    mood = random.choice(moods)
    user = random.choice(users)
    # Random time within last 10 days
    timestamp = now - timedelta(days=random.randint(0, 9), hours=random.randint(0,23), minutes=random.randint(0,59))
    mood_logs.append(MoodLog(mood=mood, timestamp=timestamp, user_id=user.id))

session.add_all(mood_logs)
session.commit()

print("Database seeded with 3 users and 30 creative mood logs!")
