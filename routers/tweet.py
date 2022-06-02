"""Tweet Routers"""
# Python
from typing import List

# FastAPI
from fastapi import APIRouter, status

# Models
from models import Tweet

router = APIRouter( prefix="/tweets")

router.tags = ["Tweets"]

# Path Operations

## Tweets
@router.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
)
def show_all_tweets():
    pass


@router.post(
    path='/',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='post a tweet',
)
def post_a_tweets():
    pass



@router.get(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a Tweet',
)
def show_an_user():
    pass


@router.delete(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a Tweet',
)
def delete_a_tweet():
    pass


@router.put(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
)
def update_a_tweet():
    pass
