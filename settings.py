from dotenv import dotenv_values
import pathlib
import os
import time
import sys

# ROOT DIRECTORY OF THE PROJECT
root_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(root_dir)

# DOTENV FILE
config = dotenv_values(f"{root_dir}/.env")

# # # #      - = TEMP KLUDGE = -    DEVELOPMENT USAGE ONLY (костыль для разработки)

if config['PRODUCTION_BUILD'] == 'True':   #### This param true/false  while docker build
    PG_HOST = config["PG_CONT_NAME"] # While docker - compose build this takes url as cont name
elif config['PRODUCTION_BUILD'] == 'False':
    PG_DOCKER_RUN_DEV_MODE = config['DOCKER_POSTGRES_UP']
    PG_HOST = config["POSTGRES_HOST_LOCAL"]  
    # N O T I C E   ---    While building app with docker-compose this part running "docker run postgres container"
    os.system(PG_DOCKER_RUN_DEV_MODE)            
    time.sleep(3)
    os.system(f'echo "Database container is up on: {PG_HOST}"')


PG_PASS = config['POSTGRES_PASSWORD']
PG_USER = config['POSTGRES_USER']
PG_DB_NAME = config['POSTGRES_DB']
SECRET_TOKEN =config['SECRET_TOKEN']
PG_PORT=config['POSTGRES_PORT']
JWT_TOKEN_LIFETIME = config['JWT_TOKEN_LIFETIME']
# REDIS cache
CACHE_EXP = config['CACHE_EXP']
REDIS_URL = config['PROD_REDIS_URL'] if config['PRODUCTION_BUILD'] == True else config['DEV_REDIS_URL']
CACHE_PREFIX = config['CACHE_PREFIX']
# JWT
ACCESS_TOKEN_EXPIRE_MINUTES = config['ACCESS_TOKEN_EXPIRE_MINUTES']
REFRESH_TOKEN_EXPIRE_MINUTES = config['REFRESH_TOKEN_EXPIRE_MINUTES']
ALGORITHM = config['ALGORITHM']
JWT_SECRET_KEY = config['JWT_SECRET_KEY']  
JWT_REFRESH_SECRET_KEY = config['JWT_REFRESH_SECRET_KEY']  

# uvicorn src.app:app --reload

# Open API tags 
TAGS_META = [
    {
        "name": "1 - OAuth2 Flow And UMA Methods",
        "description": "Endpoints that handling user registration, login/logout, password-reset things.",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "2 - User CRUD Methods",
        "description": "CRUD is the acronym for CREATE, READ, UPDATE and DELETE. Creation and managing persistent data elements, particularly User's",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "3 - Token Bearer Transport Routes",
        "description": "Token verification and refresh methods",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "4 - OAuth2 Connected External Services Methods",
        "description": "OAuth2 flow to request permission to access a user's data, redirect OAuth 2.0 server, etc...",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "5 - Company CRUD",
        "description": "CRUD Company Creation and managing persistent data elements, particularly Company's",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "6 - Employee CRUD",
        "description": "CRUD Creation and managing persistent data elements, particularly user's that have Employment in company",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },
    },
]