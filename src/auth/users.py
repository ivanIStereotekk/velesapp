from fastapi import APIRouter, Depends, HTTPException, Response, Request
from starlette.responses import JSONResponse
from src.models import Company
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from src.models import User, Employee
from starlette import status
from src.schemas import CompanyCreate, CompanyRead, CompanyUpdate
from src.db import AsyncSession, get_async_session
from sqlalchemy import select, update
from starlette import status
from fastapi_cache.decorator import cache as cache_decorator
from fastapi_redis_cache import cache_one_minute
from src.custom_responses import *




users_router = APIRouter(prefix="/auth",
    responses=ROUTER_API_RESPONSES_OPEN_API
)
@users_router.post('/register')
async def register():
    pass



# users backend
@users_router.post('/login')
async def login():
    pass


@users_router.get('/logout')
async def logout():
    pass



@users_router.post('/refresh')
async def refresh():
    pass