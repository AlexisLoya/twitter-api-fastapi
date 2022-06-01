"""Twitter models utilities."""
# Python
from typing import Optional
from datetime import datetime

# Pydantic
from pydantic import BaseModel, Field, validator


class TwitterModel(BaseModel):
    """Twitter base model.
    TwitterModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
    
    @validator("created_at", "updated_at", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()

    

