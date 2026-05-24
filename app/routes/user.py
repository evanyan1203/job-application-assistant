from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.utils.security import hash_password

# Create a router for user-related endpoints
router = APIRouter(prefix="/users", tags=["users"])


# user register API
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if a user with this email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the plain password before saving it
    hashed_pw = hash_password(user.password)

    # Create a new User object
    new_user = User(
        email=user.email,
        hashed_password=hashed_pw
    )

    # Save the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return the created user
    return new_user