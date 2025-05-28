from lib.db.models import User, MoodLog
from lib.helpers import get_random_suggestion
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

def view_mood_logs(user):
    print(f"\n🧾 Mood Log for {user.name}:")
    if not user.mood_logs:
        print("No mood logs found.")
        return
    for log in user.mood_logs:
        print(f"- [{log.timestamp.strftime('%Y-%m-%d %H:%M')}] Mood: {log.mood.capitalize()} | Suggestion: {log.suggestion}")


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

    while True:
        print("\nWhat would you like to do?")
        print("1. Log my mood")
        print("2. View my mood logs")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            mood = choose_mood()
            log_mood(user, mood)
        elif choice == "2":
            view_mood_logs(user)
        elif choice == "3":
            print("Goodbye! Take care of your mood 💙")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
