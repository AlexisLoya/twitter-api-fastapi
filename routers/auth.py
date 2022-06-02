"""Auth Routers"""

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
    """Signup

    This path operation register a user in the app

    Parameters: 
        - Request body parameter
            - user: UserRegister
    
    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: str
    """
    pass

@router.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login an User',
)
def login():
    pass