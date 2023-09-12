from fastapi import FastAPI, Depends, HTTPException, status
from db import get_db, engine
from models import User
from sqlalchemy.orm import Session
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/api/", status_code=200)
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/api/{user_name}", status_code=200, response_model=schemas.User)
def get_user(user_name: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user_name).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User  is not found")
    return db_user

@app.put("/api/{user_name}", response_model=schemas.User, status_code=status.HTTP_200_OK)
async def update_user(user_name: str, new_user: schemas.User, db: Session = Depends(get_db) ):
    db_user = db.query(User).filter(User.name == user_name).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User  is not found")
    db_user.name = new_user.name
    db.commit()
    return db_user

@app.delete("/api/{user_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_name: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user_name).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User  is not found")
    db.delete(db_user)
    db.commit()
    return