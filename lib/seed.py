# lib/seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Game
from faker import Faker
import random

# Create an engine and a session
engine = create_engine('sqlite:///migrations_test.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear the database
session.query(Game).delete()
session.commit()

# Add seed data
fake = Faker()

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

session.bulk_save_objects(games)
session.commit()

print("Database seeded!")
