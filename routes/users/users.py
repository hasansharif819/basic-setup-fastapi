from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from crud.users.users import get_user, get_users, update_user
from database.db import get_db
from schemas.users.users import UserSchema

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def get_all_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: AsyncSession = Depends(get_db)
):
    return await get_users(db, skip, limit)

@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
async def update_user_by_id(user_id: int, user: UserSchema, db: AsyncSession = Depends(get_db)):
    return await update_user(db, user_id, user)