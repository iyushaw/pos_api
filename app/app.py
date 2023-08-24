import os
from dotenv import load_dotenv
from typing import List
from fastapi import FastAPI, HTTPException, status, Path
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schemas import (
    GetUsers,
    GetUser,
    CreateUser,
    UserResponse,
    UpdateUser,
    GetCustomers,
    CreateCustomer,
    UpdateCustomer,
    CustomerResponse,
    GetCustomer,
)
from models import User, Customer

app = FastAPI()

load_dotenv(".env")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

##############################################################################
#                                                                            #
#                                   Users Route                              #
#                                                                            #
##############################################################################


# Get All Users
@app.get(
    "/api/users",
    response_model=List[GetUsers],
    status_code=status.HTTP_200_OK,
    tags=["Users"],
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
    tags=["Users"],
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
@app.get("/api/users/{id}", response_model=GetUser, status_code=200, tags=["Users"])
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
    tags=["Users"],
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


# Delete a User
@app.delete("/api/users/{id}", tags=["Users"])
async def delete_user(id: int = Path(..., title="User ID")):
    try:
        user = db.session.query(User).filter(User.user_id == id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"User with ID: {id} does not exist.",
            )
        db.session.delete(user)
        db.session.commit()
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        db.session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


##############################################################################
#                                                                            #
#                                   Customer Route                           #
#                                                                            #
##############################################################################


# Get all Customers
@app.get(
    "/api/customers",
    response_model=List[GetCustomers],
    status_code=status.HTTP_200_OK,
    tags=["Customers"],
)
async def get_all_customers():
    try:
        customer = db.session.query(Customer).all()

        return customer
    except Exception as e:
        db.session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# Add new Customer
@app.post(
    "/api/customers",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCustomer,
    tags=["Customers"],
)
async def create_customer(customer: CreateCustomer):
    try:
        new_customer = Customer(
            customer_code=customer.customer_code,
            customer_name=customer.customer_name,
            contact=customer.contact,
            address=customer.address,
        )
        print(new_customer)
        db.session.add(new_customer)
        db.session.commit()
        # db.session.close()
        return new_customer
    except Exception as e:
        # Rollback the session in case of an error
        db.session.rollback()
        # Handle the exception, you can log the error or raise a custom exception
        raise HTTPException(status_code=500, detail=str(e))


# Get one Customer
@app.get(
    "/api/customer/{id}",
    response_model=GetCustomer,
    status_code=200,
    tags=["Customers"],
)
async def get_customer(id: int = Path(..., title="Customer ID")):
    try:
        customer = db.session.query(Customer).filter(Customer.customer_id == id).first()
        if not customer:
            raise HTTPException(status_code=404, detail="User not found")
        return customer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update Customer
@app.put(
    "/api/customer/{id}",
    response_model=CustomerResponse,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Customers"],
)
async def update_customer(
    id: int = Path(..., title="Customer ID"), data: UpdateCustomer = None
):
    try:
        customer = db.session.query(Customer).filter(Customer.customer_id == id).first()
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer with ID: {id} not found",
            )

        for attr, value in data.dict().items():
            setattr(customer, attr, value)

        db.session.commit()
        db.session.refresh(customer)
        return customer
    except Exception as e:
        db.session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


# Delete a Customer
@app.delete("/api/customer/{id}", tags=["Customers"])
async def delete_customer(id: int = Path(..., title="Customer ID")):
    try:
        customer = db.session.query(Customer).filter(Customer.customer_id == id).first()

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Customer with ID: {id} does not exist.",
            )
        db.session.delete(customer)
        db.session.commit()
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        db.session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
