from lib.db.models import User, Suggestion
from lib.db.create import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Create a user (or get an existing one)
user = session.query(User).filter_by(name="Christina").first()
if not user:
    user = User(name="Christina")
    session.add(user)
    session.commit()

# Create a suggestion linked to this user
new_suggestion = Suggestion(text="Practice mindfulness meditation", mood="Calm", user_id=user.id)
session.add(new_suggestion)
session.commit()

print("Suggestion saved:", new_suggestion.text)

# Query/prints all suggestions and print them with user info from each suggestion
suggestions = session.query(Suggestion).all()
for s in suggestions:
     print(f"Suggestion: {s.text}, Mood: {s.mood}, User: {s.user.name if s.user else 'No user'}")
