# Python
from datetime import date
from typing import Optional
from uuid import UUID
# Pydantic
from pydantic import Field

# Models
from utils import TwitterModel
from models import user

class User(TwitterModel):
    tweet_id: UUID = Field(...)
    content: str = Field( 
        ...,
        min_length=1,
        max_length=280,
    )
    by:user = Field(...)