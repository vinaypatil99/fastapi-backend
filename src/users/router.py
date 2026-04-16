from fastapi import APIRouter,Depends,status,Request
from src.users.dtos import UserDTO,UserResponseDTO,LoginDTO
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.users import controller


user_routes = APIRouter(prefix="/user", tags=["Users"])


@user_routes.post("/register",response_model= UserResponseDTO,status_code= status.HTTP_201_CREATED)
def register(body : UserDTO,db : Session = Depends(get_db)):
    return controller.register(body,db)


@user_routes.post("/login",status_code= status.HTTP_200_OK)
def login_user(body : LoginDTO,db : Session = Depends(get_db)):
    return controller.login_user(body,db)


@user_routes.get("/is_auth",response_model= UserResponseDTO,status_code= status.HTTP_200_OK)
def is_auth(request : Request,db : Session = Depends(get_db)):
    return controller.is_authenticated(request,db)