# Python
from uuid import UUID
# Pydantic
from pydantic import Field

# Models
from utils import TwitterModel
from models import User

class Tweet(TwitterModel):
    tweet_id: UUID = Field(...)
    content: str = Field( 
        ...,
        min_length=1,
        max_length=280,
    )
    by:User = Field(...)