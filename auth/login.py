from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users.users import Users
from auth.security import verify_password, create_access_token
from schemas.users.users import LoginRequest

async def login_user(data: LoginRequest, db: AsyncSession):
    stmt = select(Users).where(Users.email == data.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token(data={"email": user.email, "id": user.id, "role": user.role})
    response_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
    }
    return {
        "access_token": token, 
        "token_type": "bearer",
        "user": response_user
        }
