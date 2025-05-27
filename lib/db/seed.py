from models import User, MoodLog, engine, Quote
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random

Session = sessionmaker(bind=engine)
session = Session()

quotes = [
    Quote(mood="Sad", text="Tough times don’t last. Tough people do."),
    Quote(mood="Happy", text="Happiness is only real when shared."),
    Quote(mood="Anxious", text="Just breathe. You are strong."),
]
session.add_all(quotes)
session.commit()
print("Quotes seeded successfully!")

session.query(MoodLog).delete()
session.query(User).delete()
session.commit()

users = [
    User(name="Christina"),
    User(name="James"),
    User(name="Aisha"),
]
session.add_all(users)
session.commit()


moods = [
    "Happy", "Sad", "Excited", "Anxious", "Calm",
    "Energetic", "Tired", "Frustrated", "Hopeful", "Content",
    "Nervous", "Relaxed", "Overwhelmed", "Inspired", "Lonely",
    "Grateful", "Bored", "Confident", "Restless", "Curious"
]


mood_logs = []



from datetime import datetime, timezone
now = datetime.now(timezone.utc)

for i in range(30):  
    mood = random.choice(moods)
    user = random.choice(users)

    timestamp = now - timedelta(days=random.randint(0, 9), hours=random.randint(0,23), minutes=random.randint(0,59))
    mood_logs.append(MoodLog(mood=mood, timestamp=timestamp, user_id=user.id))

session.add_all(mood_logs)
session.commit()

print("Database seeded with 3 users and 30 creative mood logs!")
