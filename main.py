# FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    """AI is creating summary for home
    """
    return {"Twitter-API":"working"}