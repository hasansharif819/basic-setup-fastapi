from pydantic import BaseModel, EmailStr
from models import *
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    role: Optional[str]
    dob: str
    gender: str
    # phone: Optional[str] = None
    
    class Config:
        orm_mode = True
        
class LoginRequest(BaseModel):
    email: EmailStr
    password: str