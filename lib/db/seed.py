import os
import sys
import random
from datetime import datetime, timedelta, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure access to project modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from lib.db.models import User, MoodLog, Quote, Suggestion
from lib.db.base import Base

# Set up database engine and session
engine = create_engine("sqlite:///lib/db/moodmate.db")
Session = sessionmaker(bind=engine)
session = Session()

def seed_quotes():
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

def clear_existing_data():
    session.query(MoodLog).delete()
    session.query(Suggestion).delete()
    session.query(User).delete()
    session.commit()
    print("🧹 Cleared existing data.")

def seed_users():
    users = [
        User(name="Christina"),
        User(name="James"),
        User(name="Aisha"),
    ]
    session.add_all(users)
    session.commit()
    print("Users seeded successfully!")
    return users

def seed_mood_logs(users):
    moods = [
        "Happy", "Sad", "Excited", "Anxious", "Calm", "Energetic", "Tired", "Frustrated",
        "Hopeful", "Content", "Nervous", "Relaxed", "Overwhelmed", "Inspired", "Lonely",
        "Grateful", "Bored", "Confident", "Restless", "Curious"
    ]
    now = datetime.now(timezone.utc)
    mood_logs = [
        MoodLog(
            mood=random.choice(moods),
            timestamp=now - timedelta(days=random.randint(0, 9), hours=random.randint(0, 23), minutes=random.randint(0, 59)),
            user_id=random.choice(users).id
        )
        for _ in range(30)
    ]
    session.add_all(mood_logs)
    session.commit()
    print("Mood logs seeded successfully!")

def seed_suggestions():
    suggestions_data = [
        {"mood": "Happy", "text": "Share your joy with someone you care about."},
        {"mood": "Sad", "text": "Watch a comforting movie or write your feelings down."},
        {"mood": "Excited", "text": "Channel that energy into a fun project or activity."},
        {"mood": "Anxious", "text": "Try a breathing exercise: in for 4, hold for 7, out for 8."},
        {"mood": "Calm", "text": "Enjoy the peace — maybe take a walk in nature or read a book."},
        {"mood": "Energetic", "text": "Use that energy! Go for a jog or dance to your favorite song."},
        {"mood": "Tired", "text": "Listen to a calming playlist or take a short nap if you can."},
        {"mood": "Frustrated", "text": "Step away and do a quick physical activity to reset."},
        {"mood": "Hopeful", "text": "Write down your goals and one small step to take today."},
        {"mood": "Content", "text": "Savor this moment with a quiet gratitude practice."},
        {"mood": "Nervous", "text": "Visualize a positive outcome. You've got this."},
        {"mood": "Relaxed", "text": "Stretch your body and enjoy the feeling of ease."},
        {"mood": "Overwhelmed", "text": "Make a quick list and tackle just one task at a time."},
        {"mood": "Inspired", "text": "Jot down your ideas while they're fresh!"},
        {"mood": "Lonely", "text": "Send a message to someone you haven't talked to in a while."},
        {"mood": "Grateful", "text": "Write down three things you're thankful for today."},
        {"mood": "Bored", "text": "Try a new hobby, recipe, or free online course."},
        {"mood": "Confident", "text": "Use your momentum to take on a small challenge."},
        {"mood": "Restless", "text": "Take a brisk walk or reorganize something in your space."},
        {"mood": "Curious", "text": "Watch a short documentary or read an article on a topic you love."}
    ]
    session.add_all([Suggestion(text=s["text"], mood=s["mood"]) for s in suggestions_data])
    session.commit()
    print("Mood-specific suggestions seeded.")

if __name__ == "__main__":
    clear_existing_data()
    seed_quotes()
    users = seed_users()
    seed_mood_logs(users)
    seed_suggestions()
    print(" Database seeding complete!")
