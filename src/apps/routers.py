from fastapi import APIRouter
from src.apps.websockets.endpoints import socket_router

api_router = APIRouter()
api_router.include_router(socket_router, prefix='/sockets', tags=["sockets"])

