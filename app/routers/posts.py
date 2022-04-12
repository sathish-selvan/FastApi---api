from app import oauth2
from .. import models, schemas, utils, oauth2
from fastapi import  FastAPI, Response,status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import engine, get_db
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# @router.get("/", response_model=List[schemas.PostOut])
@router.get("/", response_model=List[schemas.PostOut])
async def getPost(db: Session = Depends(get_db),limit:int=10, skip:int=0):
    # cursor.execute("""SELECT * FROM public."Posts" """)
    # posts = cursor.fetchall()
    # posts = db.query(models.Post).limit(limit).offset(skip).all()
    posts = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).limit(limit).offset(skip).all()
    return posts

@router.post("/", response_model=schemas.PostResponse)
async def createPost(posts:schemas.PostCreate,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO public."Posts" (title,content, published) VALUES (%s, %s, %s) RETURNING *""", (posts.title, posts.content, posts.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    new_post = models.Post(owner_id=current_user.id,**posts.dict()) 
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id:int,db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM public."Posts" WHERE id= %s """, (str(id)))
    # post = cursor.fetchone()
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unable to update")
    
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM public.'Posts' WHERE id=%=s""",(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform delete post operation")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post:schemas.PostCreate,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE public."Posts" SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""",(post.title, post.content, post.published, str(id)))
    # updatedPost = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_obj = post_query.first()
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')
    if post_obj.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform update post operation")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()