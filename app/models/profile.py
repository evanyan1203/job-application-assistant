# Import column types and ForeignKey
from sqlalchemy import Column, ForeignKey, Integer, String

# Import relationship function for table relationships
from sqlalchemy.orm import relationship

# Import Base class
from app.core.database import Base


# Define Profile table
class Profile(Base):

    # Table name in database
    __tablename__ = "profiles"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key linking this profile to a user
    # user_id must match users.id
    # unique=True means one user can only have one profile
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    # Basic profile fields
    full_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)

    # Relationship to User model
    # Allows us to access the linked user object
     # Relationship back to User
    user = relationship("User", back_populates="profile")