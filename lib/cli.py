from db.models import User, MoodLog
from helpers import get_random_suggestion
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///lib/db/moodmate.db")
Session = sessionmaker(bind=engine)
session = Session()

def user_login_or_register():
    name = input("Enter your name: ").strip()
    user = session.query(User).filter_by(name=name).first()
    if not user:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"New user '{name}' created!")
    else:
        print(f"Welcome back, {name}!")
    return user

def choose_mood():
    print("\nHow are you feeling today?")
    moods = ["happy", "sad", "angry", "jovial", "anxious"]
    for i, mood in enumerate(moods, start=1):
        print(f"{i}. {mood}")
    choice = int(input("Select a mood by number: "))
    return moods[choice - 1]

def log_mood(user, mood):
    suggestion = get_random_suggestion(mood)
    mood_log = MoodLog(user_id=user.id, mood=mood, suggestion=suggestion)
    session.add(mood_log)
    session.commit()
    print(f"\nSuggestion for you: {suggestion}")
    print("Your mood has been logged.\n")

def main():
    print("🧠 Welcome to MoodMate 🧠")
    user = user_login_or_register()
    mood = choose_mood()
    log_mood(user, mood)

if __name__ == "__main__":
    main()
