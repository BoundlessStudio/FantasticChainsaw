from fastapi import APIRouter
from app.api.endpoints import agents

api_router = APIRouter()
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
