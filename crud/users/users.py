from sqlalchemy.ext.asyncio import AsyncSession
from models.users.users import Users
from schemas.users.users import UserSchema
import models, schemas
from fastapi import HTTPException
from sqlalchemy import desc, select

async def get_user(db: AsyncSession, id: int):
    result = await db.execute(
        select(Users).where(Users.id == id)
    )
    
    db_user = result.scalar_one_or_none()
    
    res_user = {
        "name": db_user.name,
        "email": db_user.email,
        "phone": db_user.phone,
        "dob": db_user.dob,
        "gender": db_user.gender
    }
    return res_user

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(Users).offset(skip).limit(limit)
    )
    
    db_user = result.scalars().all()
    
    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "dob": user.dob,
            "gender": user.gender
        }
        for user in db_user
    ]

async def update_user(db: AsyncSession, id: int, updated_user: UserSchema):

    result = await db.execute(select(Users).where(Users.id == id))
    
    db_user = result.scalar_one_or_none()

    if not db_user:
        return HTTPException(status_code=404, detail="User not found...")  # Record does not exist

    db_user.name = updated_user.name
    db_user.email = updated_user.email
    db_user.phone = updated_user.phone
    db_user.dob = updated_user.dob
    db_user.gender = updated_user.gender
    

    await db.commit()
    await db.refresh(db_user)
    
    res_user = {
        "name": db_user.name,
        "email": db_user.email,
        "phone": db_user.phone,
        "dob": db_user.dob,
        "gender": db_user.gender
    }

    return res_user