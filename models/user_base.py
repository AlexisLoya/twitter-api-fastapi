# Python
from uuid import UUID

# Pydantic
from pydantic import EmailStr, Field

# Models
from utils import TwitterModel


class UserBase(TwitterModel): 
    user_id: UUID = Field(...)
    user_name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        example='eseloya',
    )
    email: EmailStr = Field(
        ...,
        example='eseloya@twitter.com'
        )