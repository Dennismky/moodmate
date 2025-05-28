
from models import Base, engine

# creating all tables in the database
Base.metadata.create_all(engine)

print("Tables created succesfully!")