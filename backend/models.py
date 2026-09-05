from sqlalchemy import Boolean, Column, Integer, String, text
from database import Base

class UserAccount(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    # phone_number must be unique so users can't register twice
    phone_number = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, server_default=text("true"), nullable=False)