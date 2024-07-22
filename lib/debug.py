# lib/debug.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game

# Create an engine and a session
engine = create_engine('sqlite:///../lib/migrations_test.db')  # Ensure the correct path to your database
Session = sessionmaker(bind=engine)
session = Session()

# Query the database
games_count = session.query(Game).count()
print(f"Number of games in the database: {games_count}")

first_game = session.query(Game).first()
print(f"First game: {first_game}")

last_game = session.query(Game).order_by(Game.id.desc()).first()
print(f"Last game: {last_game}")
