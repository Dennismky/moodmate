import sys
import os
import random
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.models import User, MoodLog, Quote
from lib.helpers import get_random_suggestion
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Database setup
engine = create_engine("sqlite:///lib/db/moodmate.db")
Session = sessionmaker(bind=engine)
session = Session()

# ------------------ Core Functions ------------------

def show_random_quote():
    quotes = session.query(Quote).all()
    if quotes:
        quote = random.choice(quotes)
        print(f"\nQuote of the day:\n\"{quote.text}\"")

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
    moods = [
        "happy", "sad", "angry", "jovial", "anxious",
        "energetic", "tired", "frustrated", "hopeful", "content",
        "nervous", "relaxed", "overwhelmed", "inspired", "lonely",
        "grateful", "bored", "confident", "restless", "curious"
    ]
    for i, mood in enumerate(moods, start=1):
        print(f"{i}. {mood}")
    try:
        choice = int(input("Select a mood by number: "))
        if 1 <= choice <= len(moods):
            return moods[choice - 1]
        else:
            print("Invalid number. Try again.")
            return choose_mood()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return choose_mood()

def log_mood(user, mood):
    suggestion = get_random_suggestion(mood)
    mood_log = MoodLog(user_id=user.id, mood=mood, suggestion=suggestion, timestamp=datetime.now())
    session.add(mood_log)
    session.commit()
    print(f"\nSuggestion for you: {suggestion}")
    print("Your mood has been logged.\n")

def view_mood_logs(user):
    print(f"\nMood Log for {user.name}:")
    logs = session.query(MoodLog).filter_by(user_id=user.id).order_by(MoodLog.timestamp.desc()).all()
    if not logs:
        print("No mood logs found.")
    else:
        for log in logs:
            print(f"{log.id}. [{log.timestamp.strftime('%Y-%m-%d %H:%M')}] Mood: {log.mood.capitalize()} | Suggestion: {log.suggestion}")

def delete_mood(user):
    view_mood_logs(user)
    try:
        mood_id = int(input("\nEnter the ID of the mood you want to delete: "))
        mood_log = session.query(MoodLog).filter_by(id=mood_id, user_id=user.id).first()
        if mood_log:
            session.delete(mood_log)
            session.commit()
            print("Mood log deleted successfully.")
        else:
            print("Mood ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def update_mood_log(user):
    view_mood_logs(user)
    try:
        mood_id = int(input("\nEnter the ID of the mood log to update: "))
        mood_log = session.query(MoodLog).filter_by(id=mood_id, user_id=user.id).first()
        if mood_log:
            new_mood = choose_mood()
            new_suggestion = get_random_suggestion(new_mood)
            mood_log.mood = new_mood
            mood_log.suggestion = new_suggestion
            mood_log.timestamp = datetime.now()
            session.commit()
            print("Mood log updated successfully.")
        else:
            print("Mood ID not found.")
    except ValueError:
        print("Invalid input.")

def delete_user(user):
    confirm = input(f"\nAre you sure you want to delete user '{user.name}' and all their mood logs? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(user)
        session.commit()
        print("User deleted successfully.")
        return True
    return False

def filter_mood_logs(user):
    mood_filter = input("Enter the mood to filter by (e.g., happy, sad): ").strip().lower()
    logs = session.query(MoodLog).filter_by(user_id=user.id, mood=mood_filter).order_by(MoodLog.timestamp.desc()).all()
    if not logs:
        print("No mood logs found for that mood.")
    else:
        for log in logs:
            print(f"{log.id}. [{log.timestamp.strftime('%Y-%m-%d %H:%M')}] Mood: {log.mood.capitalize()} | Suggestion: {log.suggestion}")

#  Main CLI 

def main():
    print("Welcome to MoodMate CLI")
    show_random_quote()
    user = user_login_or_register()

    while True:
        print("\nWhat would you like to do?")
        print("1. Log my mood")
        print("2. View my mood logs")
        print("3. Update a mood log")
        print("4. Delete a mood log")
        print("5. Filter mood logs")
        print("6. Delete my user account")
        print("7. Exit")
        choice = input("Enter choice (1-7): ")

        if choice == "1":
            mood = choose_mood()
            log_mood(user, mood)
        elif choice == "2":
            view_mood_logs(user)
        elif choice == "3":
            update_mood_log(user)
        elif choice == "4":
            delete_mood(user)
        elif choice == "5":
            filter_mood_logs(user)
        elif choice == "6":
            if delete_user(user):
                break
        elif choice == "7":
            print("Goodbye! Take care of your mood 💙")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
