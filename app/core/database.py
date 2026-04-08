# Import function to create database engine (connection)
from sqlalchemy import create_engine

# Import ORM tools: Base class and session factory
from sqlalchemy.orm import declarative_base, sessionmaker


# Database URL
# sqlite:/// means using SQLite
# ./job_assistant.db means the file is in the current directory
DATABASE_URL = "sqlite:///./job_assistant.db"


# Create database engine (core connection object)
engine = create_engine(
    DATABASE_URL,

    # Required for SQLite to allow multi-thread access
    connect_args={"check_same_thread": False}
)


# Create a session factory
# Each request will use a session to interact with DB
SessionLocal = sessionmaker(
    autocommit=False,   # We manually commit changes
    autoflush=False,    # Don't auto-sync changes
    bind=engine         # Bind session to engine
)


# Base class for all ORM models
# All tables must inherit from this
Base = declarative_base()


# Dependency function for FastAPI
# Provides a database session per request
def get_db():
    db = SessionLocal()   # Create new session
    try:
        yield db          # Provide session to endpoint
    finally:
        db.close()        # Always close session after request