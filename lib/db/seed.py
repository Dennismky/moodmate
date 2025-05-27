from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, MoodLog

engine = create_engine('sqlite:///moodmate.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating test user and mood logs
user = User(name="Christina")
session.add(user)
session.commit()

mood1 = MoodLog(mood="Happy", user_id=user.id)
mood2 = MoodLog(mood="Stressed", user_id=user.id)

session.add_all([mood1, mood2])
session.commit()
print("Seeded database!")
