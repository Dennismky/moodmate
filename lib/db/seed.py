
from models import  MoodLog,engine

from models import User, MoodLog, engine, Quote

from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, timezone
from lib.db.create import engine, Base
from lib.db.models import Suggestion, User


import random

Session = sessionmaker(bind=engine)
session = Session()


quotes = [
    Quote(mood="Happy", text="Happiness is only real when shared."),
    Quote(mood="Sad", text="Tough times do not last. Tough people do."),
    Quote(mood="Excited", text="Let your excitement be greater than your fear."),
    Quote(mood="Anxious", text="Just breathe. You are strong."),
    Quote(mood="Calm", text="Peace begins with a deep breath."),
    Quote(mood="Energetic", text="Energy and persistence conquer all things."),
    Quote(mood="Tired", text="Rest is not a waste of time; it is how you grow stronger."),
    Quote(mood="Frustrated", text="Frustration is a sign of ambition. Take a step back."),
    Quote(mood="Hopeful", text="Hope is the thing with feathers that perches in the soul."),
    Quote(mood="Content", text="Contentment is not the fulfillment of what you want, but the realization of how much you already have."),
    Quote(mood="Nervous", text="Nerves are a sign you care. Use that energy."),
    Quote(mood="Relaxed", text="Relaxation is the gateway to clarity."),
    Quote(mood="Overwhelmed", text="You do not have to do it all at once. One step at a time."),
    Quote(mood="Inspired", text="Inspiration exists, but it has to find you working."),
    Quote(mood="Lonely", text="You are never alone. The world is full of people who care."),
    Quote(mood="Grateful", text="Gratitude turns what we have into enough."),
    Quote(mood="Bored", text="Boredom is the birthplace of creativity."),
    Quote(mood="Confident", text="Believe in yourself and the world will follow."),
    Quote(mood="Restless", text="Let your restlessness lead you to new adventures."),
    Quote(mood="Curious", text="Stay curious. It is how you learn and grow.")
]

session.add_all(quotes)
session.commit()
print("Quotes seeded successfully!")


session.query(MoodLog).delete()
session.query(Suggestion).delete()
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



now = datetime.now(timezone.utc)


mood_logs = []
for _ in range(30):
    mood = random.choice(moods)
    user = random.choice(users)
    
    timestamp = now - timedelta(days=random.randint(0, 9),
                                hours=random.randint(0, 23),
                                minutes=random.randint(0, 59))


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

print("Database seeded with 3 users and 30 mood logs!")


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
