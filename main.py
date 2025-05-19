from fastapi import FastAPI
from routes.auth import register, login
from database.db import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind = engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],             # Or use ["*"] for all origins (not safe for production)
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all headers
)

@app.get("/")
def hello():
	return {"hello": "World"}

app.include_router(register.router)
app.include_router(login.router)