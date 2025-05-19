from sqlalchemy.orm import Session, Query
from models.users.users import Users
from schemas.users.users import UserSchema
import models, schemas
from fastapi import HTTPException
from sqlalchemy import desc

def get_user(db: Session, id: int):
    return db.query(Users).filter(Users.id == id).first()

def get_users(db: Session, skip: int = 0, limit: int = Query(...)):
    return db.query(Users).offset(skip).limit(limit).all()

def update_user(db: Session, id: int, updated_user: UserSchema):

    db_user = db.query(models.UserAuth).filter(models.UserAuth.id == id).first()

    if not db_user:
        return HTTPException(status_code=404, detail="User not found...")  # Record does not exist

    db_user.name = updated_user.name
    db_user.email = updated_user.email

    db.commit()
    db.refresh(db_user)

    return db_user