# Python
from datetime import date
from typing import Optional
from uuid import UUID
# Pydantic
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length=8,
    )
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_day: Optional[date] = Field(default=None)