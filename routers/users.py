"""User Routers"""
# Python
from typing import List

# FastAPI
from fastapi import APIRouter, status

# Models
from models import User

router = APIRouter()
router.tags = ["Users"]


# Path Operations

## Users
@router.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register an User',
)
def signup():
    pass

@router.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login an User',
)
def login():
    pass

@router.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
)
def show_all_users():
    pass

@router.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show an User',
)
def show_an_user():
    pass

@router.delete(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete an User',
)
def delete_an_user():
    pass

@router.put(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update an User',
)
def update_an_user():
    pass
