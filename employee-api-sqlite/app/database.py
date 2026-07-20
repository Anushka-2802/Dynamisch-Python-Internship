"""
This file is responsible for creating the SQLite database connection
and configuring SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# SQLITE Database URL
DATABASE_URL = "sqlite:///./employee.db"

# Create databse engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create session for database operations
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

# Base class for SQLAlchemy models
Base = declarative_base()