from fastapi import  FastAPI
from src.schemas import UserCreate, UserRead, UserUpdate
from src.auth.users import users_router,user_crud,user_oauth_outer,bearer_router
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



#   R O U T E R S 
# User AUTH Routers

app.include_router(users_router,tags=['OAuth2 Flow And User Management Routes'])
app.include_router(user_crud,tags=['User CRUD Methods'])
app.include_router(user_oauth_outer,tags=['OAuth2 Connected External Services Methods'])
app.include_router(bearer_router,tags=['Token [Bearer] Transport Routes'])







# Employee Router - Imported from module employee.py
app.include_router(
    user_extender_router,tags=['Employee CRUD Methods']
    )
# company Router - cmp.py
app.include_router(
    company_router,tags=['Company CRUD Methods ']
    )




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
