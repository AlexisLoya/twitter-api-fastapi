# Pydantic
from pydantic import Field

from models.user_base import UserBase

# Models
from .user import User
from .user_base import UserBase

class PasswordMixin(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number and one special character.",
        
    )
    
    
    
class UserLogin(PasswordMixin, UserBase):
    pass
    
class UserSignIN(PasswordMixin, User):
    pass
    
    
    
    
    
    