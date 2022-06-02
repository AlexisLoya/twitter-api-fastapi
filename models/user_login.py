# Pydantic
from pydantic import Field

# Models
from .user import User

class UserLogin(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number and one special character.",
        
    )