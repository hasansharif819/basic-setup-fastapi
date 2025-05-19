from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Enum as senum
from sqlalchemy.orm import relationship
from database.db import Base
from enum import Enum

class RoleEnum(str, Enum):
    admin = 'admin'
    user = 'user'
    
class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'
    others = 'others'

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone = Column(String(15), nullable=False)
    role = Column(senum(RoleEnum), nullable=False, default=RoleEnum.user)
    dob = Column(String(15), nullable=False)
    gender = Column(senum(GenderEnum), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    is_varified = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
