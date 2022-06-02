# Python
from datetime import date
from typing import Optional

# Pydantic
from pydantic import Field, validator

# Models
from .genders import Genders
from .user_base import UserBase



class User(UserBase):

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
    birth_date: date = Field(..., example='1998-06-23')
    gender: Optional[Genders] = Field(default=None, example="Male")
    
    
    @validator('user_name')
    def name_must_not_contain_space(cls, v):
        if ' ' in v:
            raise ValueError('the username must not contain a space')
        return v.title()
    
    @validator('birth_date')
    def is_over_eighteen(cls, v):
        todays_date = date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError('Must be over 18 years old!')
        else:
            return v