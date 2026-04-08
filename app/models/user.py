# Import column and data types
from sqlalchemy import Column, Integer, String, DateTime

# Import database function utilities (e.g., current timestamp)
from sqlalchemy.sql import func

# Import Base class
from app.core.database import Base

from sqlalchemy.orm import relationship

# Define User table
class User(Base):

    # Table name in database
    __tablename__ = "users"

    # Primary key (unique identifier)
    id = Column(Integer, primary_key=True, index=True)

    # Email (must be unique and cannot be null)
    email = Column(String, unique=True, index=True, nullable=False)

    # Hashed password (never store raw password)
    hashed_password = Column(String, nullable=False)

    # Automatically store creation time
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    # One-to-one relationship with Profile
    profile = relationship("Profile", back_populates="user", uselist=False)

