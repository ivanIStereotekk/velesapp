from fastapi import  FastAPI
from src.schemas import UserCreate, UserRead, UserUpdate
from src.auth.users import auth_backend,  fastapi_users
from src.employee import ext_router as user_extender_router
from src.company import cmp_router as company_router
from settings import config
from src.db import Base 
from src.db import engine
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis
from settings import REDIS_URL,CACHE_PREFIX, TAGS_META




# OpenAPI  - P R E S E N T A T I O N    D A T A
contact_dict = dict(name=config['CONTACT_NAME'],
                    email=config['CONTACT_EMAIL'],
                                  )
app = FastAPI(title=config['API_TITLE'],description=config['API_DESCRIPTION'],contact=contact_dict,openapi_tags=TAGS_META)

# Employee Router - Imported from module employee.py
app.include_router(
    user_extender_router,tags=['Employee Methods']
    )
# company Router - cmp.py
app.include_router(
    company_router,tags=['Company Methods ']
    )

# users backend
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["Login / Logout Methods"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Register User Methods"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Reset Password Methods"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Veryfy Methods"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["User CRUD Methods"],
)


# @app.get("/drop-create",tags=['Base Migrations Method'])
# async def metadata_route(command:str = None):
#     """Dev usage cludge:
#     For making migrations use this route by writing in command query - create_all | drop_all

#     "details":\n
#                 {
#                 "drop_all": "deletes all tables in database",
#                 "create_all": "creates all tables using Metadata object."
#                 }
#     """
#     if command:
#         match command:
#             case "create_all":
#                 async with engine.begin() as conn:
#                     await conn.run_sync(Base.metadata.create_all)
#             case "drop_all":
#                 async with engine.begin() as conn:
#                     await conn.run_sync(Base.metadata.drop_all)
                    
#     return {"message": f"Hello Word!" }


import importlib
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# REDIS startup
@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix=CACHE_PREFIX)
