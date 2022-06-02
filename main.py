""" Main Aplication """

# FastAPI
from fastapi import FastAPI

# Routers
from routers import routers

## twitter-api app
app = FastAPI()

# adding routers
app.include_router(routers)



## Tweets

## Home
@app.get("/")
def home():
    """AI is creating summary for home
    """
    return {"Twitter-API":"working"}
