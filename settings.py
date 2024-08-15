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
        "name": "Users",
        "description": "***User Management Authentication[UMA]*** methods flow. Registration, Authentication, Reset password, typical UMA user flow.",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "Company",
        "description": "***Company*** ORM model and it's methods for making CRUD operations. Company - represents company item with data fields.",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },

    },
    {
        "name": "Employee",
        "description": "***Employee*** Methods for ORM model that extends User model. Employee - gives additional data structure to user that became as employee. Logically user may change the employment position so someone may substitute **user** on particular position. When particular _user_ is unemployed he has no Employee table...\nThis table extends user which works in the company on a position.",
        "externalDocs": {
            "description": "Any question?",
            "url": "https://t.me/ewanG808",
        
        },
    },
]