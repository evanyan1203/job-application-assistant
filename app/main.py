# Import FastAPI framework
from fastapi import FastAPI

# Import Base (for models) and engine (database connection)
from app.core.database import Base, engine

# IMPORTANT:
# This import ensures that the User model is registered
# If we don't import it, the table will NOT be created
from app.models import user, profile

# Create FastAPI app instance
app = FastAPI()


# Create all database tables based on models
# It scans all classes that inherit from Base
Base.metadata.create_all(bind=engine)


# Test route
@app.get("/")
def root():
    return {"message": "Job Application Assistant is running"}




from app.utils.security import hash_password, verify_password

password = "test123"

hashed = hash_password(password)
print("Hashed:", hashed)

is_valid = verify_password("test123", hashed)
print("Match:", is_valid)