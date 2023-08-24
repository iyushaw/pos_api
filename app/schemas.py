from pydantic import BaseModel
from typing import Optional, List

##############################################################################
#                                                                            #
#                                   Customer Models                          #
#                                                                            #
##############################################################################


class CreateCustomer(BaseModel):
    customer_code: str
    customer_name: str
    contact: str
    address: str


class UpdateCustomer(BaseModel):
    customer_code: str
    customer_name: str
    contact: str
    address: str


class CustomerResponse(BaseModel):
    customer_code: str
    customer_name: str
    contact: str
    address: str


class GetCustomer(BaseModel):
    customer_code: str
    customer_name: str
    contact: str
    address: str

    class Config:
        orm = True


##############################################################################
#                                                                            #
#                                   User Models                              #
#                                                                            #
##############################################################################


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


class GetCustomers(BaseModel):
    customer_id: int
    customer_code: str
    customer_name: str
    contact: str
    address: str

    class Config:
        orm = True
