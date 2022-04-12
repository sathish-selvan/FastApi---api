
from .. import models, schemas, utils
from fastapi import  FastAPI, Response,status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db

############################## User ##############################

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user : schemas.UserCreate,db:Session = Depends(get_db)):
    
    #hashing the password
    hashed_password = utils.hash(user.password) 
    user.password = hashed_password
    newuser = models.User(**user.dict())
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not count")
    return user
