from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    # Email provided by the user during registration
    email: EmailStr

    # Plain password provided by the user
    password: str


class UserResponse(BaseModel):
    # User ID from the database
    id: int

    # User email from the database
    email: EmailStr

    class Config:
        # Allows Pydantic to read SQLAlchemy model objects
        from_attributes = True