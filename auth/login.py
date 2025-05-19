from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.users.users import Users
from auth.security import verify_password, create_access_token
from schemas.users.users import LoginRequest

def login_user(data: LoginRequest, db: Session):
    user = db.query(Users).filter(Users.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token(data={"sub": user.email, "id": user.id, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
