"""Auth Routers"""
# Python
import json
from uuid import UUID
from typing import List, Dict

# FastAPI
from fastapi import APIRouter, status, Body,HTTPException

# Models
from models import User,UserSignIN

router = APIRouter( prefix="/auth")
router.tags = ["Authentication"]


# Path Operations

## Auth
@router.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register an User',
)
def signup(user:UserSignIN = Body(...)):
    """
    Signup

    This path operation register a user in the app

    Parameters: 
        - Request body parameter
            - user: UserSignIN
    
    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f: 
        results:List[str, Dict] = json.loads(f.read())
        user_dict = user.dict()
        if any(users['email'] == user.email for users in results):
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exist!"
        )
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        user_dict["created_at"] = str(user_dict["created_at"])
        user_dict["updated_at"] = str(user_dict["updated_at"])
        user_dict["gender"] = str(user_dict["gender"])[8::]
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

@router.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login an User',
)
def login():
    pass