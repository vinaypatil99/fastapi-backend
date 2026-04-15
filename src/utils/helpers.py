
from src.users.models import UserModel
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends,Request
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from src.utils.db import get_db


# This function validates the JWT token from the request header, 
# verifies the user from the database, and returns the authenticated user if the token is valid.
def is_authenticated(request : Request, db : Session= Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "User is unauthorized!!")
            
        token = token.split(" ")[-1]
        
        data = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        
        user_id = data.get("_id")
        
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "User is unauthorized!!")
            
        
        return user
    
    except InvalidTokenError:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "User is unauthorized!!")