from datetime import datetime
from os import access
from pydantic import BaseModel, EmailStr, conint
from typing import Optional


class Post(BaseModel):
    title:str
    content: str
    published : bool = True

class PostCreate(Post):
    pass

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True 

class PostResponse(Post):
    id:int
    owner_id:int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post : PostResponse
    votes : int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str



class UserLogin(UserCreate):
    pass


class Token(BaseModel):
    token: str
    token_type : str
    class Config:
        orm_mode = True 

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)