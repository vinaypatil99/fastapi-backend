from src.users.models import UserModel
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends,Request
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from src.utils.db import get_db
from pwdlib import PasswordHash
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


password_hash = PasswordHash.recommended()

# password -> hash password
def get_password_hash(password):
    return password_hash.hash(password)

# verify password plain pass and hashed pass
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


# This function validates the JWT token from the request header, 
# verifies the user from the database, and returns the authenticated user if the token is valid.
# def is_authenticated(request : Request, db : Session= Depends(get_db)):
#     try:
#         token = request.headers.get("authorization")
#         if not token:
#             raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "User is unauthorized!!")
            
#         token = token.split(" ")[-1]
        
#         data = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        
#         user_id = data.get("_id")
        
#         user = db.query(UserModel).filter(UserModel.id == user_id).first()
#         if not user:
#             raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "User is unauthorized!!")
            
        
#         return user
    
#     except InvalidTokenError:
#             raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "User is unauthorized!!")

security = HTTPBearer()


def is_authenticated(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    try:
        token = credentials.credentials  # ✅ Extract token directly

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = data.get("_id")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        return user

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
        

def require_role(required_role: str):
    def role_checker(user=Depends(is_authenticated)):
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied: insufficient permissions"
            )
        return user

    return role_checker