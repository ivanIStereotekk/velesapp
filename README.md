** Users management **

> [!NOTE]
> New fork with OAuth2 JWT implementation.
>       - working hard -


### With OAuth2 JWT implementation.
```.env

PRODUCTION_BUILD='False'
PG_CONT_NAME=postgres_db


# addres while run in local
POSTGRES_HOST_LOCAL=localhost

POSTGRES_PASSWORD=secret123
POSTGRES_USER=postgres


# If it is not specified, then the value of POSTGRES_USER will be used.
POSTGRES_DB=postgres
POSTGRES_PORT=5432
# This cmd command will run docker container
DOCKER_POSTGRES_UP='docker run -it --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=secret123 -p 5432:5432 -d postgres:latest'

# Change while production
SECRET_TOKEN=secret
JWT_REFRESH_SECRET_KEY=secretKey
JWT_SECRET_KEY=secretKey
JWT_TOKEN_LIFETIME=3600
ACCESS_TOKEN_EXPIRE_MINUTES=30  # 30 min
REFRESH_TOKEN_EXPIRE_MINUTES=10080 # 7 days
ALGORITHM ="HS256"
CACHE_EXP=3600
# Notice difference !
DEV_REDIS_URL='redis://localhost'
PROD_REDIS_URL = 'redis://redis_cache'

CACHE_PREFIX='Veles-app:'
CONTACT_NAME='Ivan Goncharov'
CONTACT_EMAIL='ivan.stereotekk@gmail.com'
API_TITLE='User Access Management  - [ web application ]'
API_DESCRIPTION='VELES - App for the build methods!'

```

