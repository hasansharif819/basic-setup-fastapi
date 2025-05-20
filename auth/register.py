from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users.users import Users
from schemas.users.users import UserSchema
from fastapi import HTTPException
from auth.security import hash_password

async def register_user(db: AsyncSession, user: UserSchema) -> Users:
    # Async select
    result = await db.execute(select(Users).where(Users.email == user.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")

    new_user = Users(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        phone=user.phone,
        role=user.role,
        dob=user.dob,
        gender=user.gender
    )
    db.add(new_user)  # no await here
    await db.commit()
    await db.refresh(new_user)
    return new_user
