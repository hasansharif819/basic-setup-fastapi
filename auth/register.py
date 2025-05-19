from sqlalchemy.orm import Session, Query
from models.users.users import Users
from schemas.users.users import UserSchema
from fastapi import HTTPException
from auth.security import hash_password

def register_user(db: Session, user: UserSchema) -> Users:
    # Check if user already exists
    existing_user = db.query(Users).filter(
        (Users.email == user.email)).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = Users(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        phone=user.phone,
        role=user.role,
        dob=user.dob,
        gender=user.gender
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user