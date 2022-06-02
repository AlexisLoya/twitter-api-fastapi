"""User Routers"""
# Python
from typing import List
import json
# FastAPI
from fastapi import APIRouter, status

# Models
from models import User

router = APIRouter( prefix="/users")
router.tags = ["Users"]


# Path Operations

## Users
@router.get(
    path='',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
)
def show_all_users():
    """
    This path operation shows all users in the app

    Parameters: 
        -

    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

@router.get(
    path='/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show an User',
)
def show_an_user():
    pass

@router.delete(
    path='/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete an User',
)
def delete_an_user():
    pass

@router.put(
    path='/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update an User',
)
def update_an_user():
    pass
