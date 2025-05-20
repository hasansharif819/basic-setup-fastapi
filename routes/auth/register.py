from fastapi import APIRouter, Depends, HTTPException
from models.users.users import Users
from schemas.users.users import UserSchema
from sqlalchemy.orm import Session
from database.db import get_db
from auth.register import register_user
from auth.security import create_email_token, verify_email_token
from utils.email import send_verification_email
from database.db import get_db


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: UserSchema, db: Session = Depends(get_db)):
    
    new_user = await register_user(db, user)
    
    # return_data = {
    #     "name": new_user.name,
    #     "email": new_user.email,
    #     "phone": new_user.phone,
    #     "role": new_user.role,
    #     "dob": new_user.dob,
    #     "gender": new_user.gender
    # }
    # return return_data
    
    token = create_email_token(user.email)
    send_verification_email(user.email, token)
    # get_db[user.email] = {"password": user.password, "is_verified": False}
    return {"message": "Verification email sent."}

@router.get("/verify-email")
def verify_email(token: str):
    email = verify_email_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    return {"message": "Email verified successfully."}