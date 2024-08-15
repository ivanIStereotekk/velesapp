from passlib.context import CryptContext
import os
import sys
from datetime import datetime as dt
from datetime import timedelta
from typing import Union, Any
from jose import jwt




from settings import JWT_REFRESH_SECRET_KEY,JWT_SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES,REFRESH_TOKEN_EXPIRE_MINUTES


# creates access token = exp date takes datetime object
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = dt.datetime.now() + expires_delta
    else:
        expires_delta = dt.datetime.now() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


# creates refresh token
def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = dt.datetime.now() + expires_delta
    else:
        expires_delta = dt.datetime.now() + timedelta(minutes=int(REFRESH_TOKEN_EXPIRE_MINUTES))
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


# password hashing (Think about !)

class HashingFactory:
    context = CryptContext(schemes=["bcrypt"])
    def __init__(self,password:str,hashed_password=None):
        self.password = password
        self.hashed_password = hashed_password
    @staticmethod
    def get_hashed_password(self):
        return self.context.hash(self.password)
    @staticmethod
    def verify_password(self) -> bool:
        return self.context.verify(self.password, self.hashed_pass)