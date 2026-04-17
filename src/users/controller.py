from src.users.dtos import UserDTO,LoginDTO
from src.users.models import UserModel
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
import jwt
from src.utils.settings import settings
from datetime import datetime,timedelta

from src.utils.security import get_password_hash, verify_password



def register(body: UserDTO, db: Session, current_user=None):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="Username already exists!!")

    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(400, detail="User email already exists!!")

    hash_password = get_password_hash(body.password)

    # RBAC logic
    role = "user"

    if body.role == "admin":
         if not current_user or current_user.role != "admin":
            raise HTTPException(403, "Only admin can create admin")
         role = "admin"

    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hash_password,
        email=body.email,
        role=role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(body : LoginDTO,db : Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found!!")
    
    if not verify_password(body.password,user.hash_password):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail= "Passwords do not match!!")
    
    exp_time = datetime.now() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    
    payload = {
        "_id": user.id,
        "role": user.role,
        "exp": exp_time.timestamp()
    }
    
    token = jwt.encode(payload,settings.SECRET_KEY,settings.ALGORITHM)
        
        
    return {"token": token}