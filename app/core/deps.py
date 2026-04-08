from app.core.database import SessionLocal
# Import the SessionLocal class (this creates a database session)


def get_db():
    """
    Dependency that provides a database session to API endpoints.
    FastAPI will call this function automatically.
    """
    
    db = SessionLocal()
    # Create a new database session (connection)

    try:
        yield db
        # Yield the session so the route can use it
        # (FastAPI dependency injection)

    finally:
        db.close()
        # Always close the session after the request finishes
        # Prevents memory leaks and connection issues