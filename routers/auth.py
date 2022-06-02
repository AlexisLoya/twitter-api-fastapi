"""Auth Routers"""
# Python
from typing import List

# FastAPI
from fastapi import APIRouter, status

# Models
from models import User

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