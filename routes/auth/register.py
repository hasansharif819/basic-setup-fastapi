from fastapi import APIRouter, Depends
from models.users.users import Users
from schemas.users.users import UserSchema
from sqlalchemy.orm import Session
from database.db import get_db
from auth.register import register_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserSchema, db: Session = Depends(get_db)):
    
    new_user = register_user(db, user)

    return_data = {
        "name": new_user.name,
        "email": new_user.email,
        "phone": new_user.phone,
        "role": new_user.role,
        "dob": new_user.dob,
        "gender": new_user.gender
    }
    return return_data
