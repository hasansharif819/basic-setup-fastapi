from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import register, login
from database.db import Base, engine  # assumes async engine
from sqlalchemy.ext.asyncio import AsyncEngine

app = FastAPI()

# Enable CORS (you can restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins - restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def hello():
    return {"hello": "World"}

# Async startup event to create tables
@app.on_event("startup")
async def startup():
    if isinstance(engine, AsyncEngine):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

# Include your route files
app.include_router(register.router)
app.include_router(login.router)

