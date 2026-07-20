"""
This file creates and closes the database session
for every API request
"""
from database import SessionLocal

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()