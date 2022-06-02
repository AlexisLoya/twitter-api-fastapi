from fastapi import APIRouter

from .users import router as user_routers
from .tweet import router as tweet_routers
from .auth import router as auth_routers

routers = APIRouter(
    prefix="/api"
)

routers.include_router(user_routers)
routers.include_router(tweet_routers)
routers.include_router(auth_routers)