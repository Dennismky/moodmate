from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, MoodLog
from datetime import datetime
from sqlalchemy.orm import Session
from lib.db.models import Suggestion


# Connecting to the database
db_path = 'lib/db/moodmate.db'
engine = create_engine(f'sqlite:///lib/db/moodmate.db')
Session = sessionmaker(bind=engine)
session = Session()




def create_mood_log(user_name, mood):
    user = session.query(User).filter_by(name=user_name).first()
    if not user:
        print(f"User '{user_name}' not found.")
        return
    new_log = MoodLog(mood=mood, timestamp=datetime.now(), user_id=user.id)
    session.add(new_log)
    session.commit()
    print(f"Mood '{mood}' added for user '{user_name}'")



def read_mood_logs(user_name=None):
    if user_name:
        logs = session.query(MoodLog).join(User).filter(User.name == user_name).all()
    else:
        logs = session.query(MoodLog).all()
    for log in logs:
        user = session.query(User).filter_by(id=log.user_id).first()
        print(f"{user.name}: {log.mood} at {log.timestamp}")




def update_mood_log(log_id, new_mood):
    log = session.query(MoodLog).filter_by(id=log_id).first()
    if not log:
        print(f"Mood log with ID {log_id} not found.")
        return
    log.mood = new_mood
    session.commit()
    print(f"Updated mood log ID {log_id} to '{new_mood}'")



def delete_mood_log(log_id):
    log = session.query(MoodLog).filter_by(id=log_id).first()
    if not log:
        print(f"Mood log with ID {log_id} not found.")
        return
    session.delete(log)
    session.commit()
    print(f"Deleted mood log ID {log_id}")





def create_suggestion(db_session, text, mood=None, user_name=None):
    user = None
    if user_name:
        user = db_session.query(User).filter_by(name=user_name).first()
        if not user:
            print(f"Warning: User '{user_name}' not found. Suggestion will have no user.")
    suggestion = Suggestion(text=text, mood=mood, user_id=user.id if user else None)
    db_session.add(suggestion)
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error adding suggestion: {e}")
        return None
    print("Suggestion added.")
    return suggestion

def read_suggestions(db_session, mood=None):
    query = db_session.query(Suggestion)
    if mood:
        query = query.filter(Suggestion.mood == mood)
    suggestions = query.all()
   
    for s in suggestions:
        print(f"{s.text} (Mood: {s.mood}, User: {s.user.name if s.user else 'General'})")
    return suggestions
