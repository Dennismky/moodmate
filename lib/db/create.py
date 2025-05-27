
from models import Base, engine, Quote


Base.metadata.create_all(engine)

print("Tables created succesfully!")