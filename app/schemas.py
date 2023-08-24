from pydantic import BaseModel
from typing import Optional, List


class CreateUser(BaseModel):
    username: str
    password: str
    fullname: str
    designation: int
    contact: str
    account_type: int

    class Config:
        orm = True


class GetUsers(BaseModel):
    username: str
    password: str
    fullname: str
    designation: int
    contact: str
    account_type: int

    class Config:
        orm = True


class GetUser(BaseModel):
    username: str
    password: str
    fullname: str
    designation: int
    contact: str
    account_type: int

    class Config:
        orm = True


class UpdateUser(BaseModel):
    username: str
    password: str
    fullname: str
    designation: int
    contact: str
    account_type: int


class UserResponse(BaseModel):
    user_id: int
    username: str
    password: str
    fullname: str
    designation: int
    contact: str
    account_type: int
