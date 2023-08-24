from fastapi import FastAPI, Depends, HTTPException, status, Path
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import GetUsers, GetUser, CreateUser, UserResponse, UpdateUser
from dotenv import load_dotenv
from models import User
import sys
import os
from typing import List

app = FastAPI()

load_dotenv(".env")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# Get All Users
@app.get(
    "/api/users",
    response_model=List[GetUsers],
    status_code=status.HTTP_200_OK,
    tags=["users"],
)
async def get_all_users():
    try:
        users = db.session.query(User).all()

        return users
    except Exception as e:
        db.session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# Create a New User
@app.post(
    "/api/users",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateUser,
    tags=["users"],
)
async def create_user(user: CreateUser):
    try:
        new_user = User(
            username=user.username,
            password=user.password,
            fullname=user.fullname,
            designation=user.designation,
            contact=user.contact,
            account_type=user.account_type,
        )

        db.session.add(new_user)
        db.session.commit()
        # db.session.close()
        return new_user
    except Exception as e:
        # Rollback the session in case of an error
        db.session.rollback()
        # Handle the exception, you can log the error or raise a custom exception
        raise HTTPException(status_code=500, detail=str(e))


# Get one User
@app.get("/api/users/{id}", response_model=GetUser, status_code=200, tags=["users"])
async def get_user(id: int = Path(..., title="User ID")):
    try:
        user = db.session.query(User).filter(User.user_id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update User
@app.put(
    "/api/users/{id}",
    response_model=UserResponse,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["users"],
)
async def update_user(id: int = Path(..., title="User ID"), data: UpdateUser = None):
    try:
        user = db.session.query(User).filter(User.user_id == id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        for attr, value in data.dict().items():
            setattr(user, attr, value)

        db.session.commit()
        db.session.refresh(user)
        return user
    except Exception as e:
        db.session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
