""" Main Aplication """

# FastAPI
from fastapi import FastAPI

# Routers
from routers import user_routers
from routers import tweet_routers

## twitter-api app
app = FastAPI()

# adding routers
app.include_router(user_routers)
app.include_router(tweet_routers)



## Tweets

## Home
@app.get("/")
def home():
    """AI is creating summary for home
    """
    return {"Twitter-API":"working"}
