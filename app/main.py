from fastapi import  FastAPI
from .database import engine
from . import models
from . routers import posts, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from app import database



# models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello bro"}



