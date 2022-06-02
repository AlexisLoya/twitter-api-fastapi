"""Tweet Routers"""
# Python
from typing import List
import json
# FastAPI
from fastapi import APIRouter, status, Body

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
    """
    This path operation shows all tweets in the app

    Parameters: 
        -

    Returns a json list with all users in the app, with the following keys: 
        - tweet_id: UUID
    """
    with open("tweets.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

@router.post(
    path='/',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='post a tweet',
)
def post_a_tweets(tweet: Tweet = Body(...)):
    """
    Post a Tweet
    This path operation post a tweet in the app
    Parameters: 
        - Request body parameter
            - tweet: Tweet
    
    Returns a json with the basic tweet information: 
        tweet_id: UUID  
        content: str    
        created_at: datetime
        updated_at: Optional[datetime]
        by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        tweet_dict["by"]["created_at"] = str(tweet_dict["by"]["created_at"])
        tweet_dict["by"]["updated_at"] = str(tweet_dict["by"]["updated_at"])
        tweet_dict["by"]["gender"] = str(tweet_dict["by"]["gender"])[8::]
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet    





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
