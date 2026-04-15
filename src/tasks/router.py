from fastapi import APIRouter,status
from src.tasks import controller
from src.tasks.dtos import TaskDTO,TaskResponseDTO
from src.users.models import UserModel
from fastapi import Depends
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated

task_routes = APIRouter(prefix="/tasks")

# create new task
@task_routes.post("/create",response_model= TaskResponseDTO, status_code= status.HTTP_201_CREATED)
def create_task(body : TaskDTO, db : Session = Depends(get_db),user : UserModel = Depends(is_authenticated)):
    return controller.create_task(body,db,user)


# get all tasks
@task_routes.get("/all_tasks",response_model= List[TaskResponseDTO],status_code= status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db),user : UserModel = Depends(is_authenticated)):
    return controller.get_all_tasks(db,user)


# get task by id
@task_routes.get("/get_by_id/{id}",response_model= TaskResponseDTO,status_code= status.HTTP_200_OK)
def get_by_id(id : int,db:Session = Depends(get_db),user : UserModel = Depends(is_authenticated)):
    return controller.get_by_id(id,db)


# update task by id
@task_routes.put("/update_task/{id}",response_model= TaskResponseDTO,status_code= status.HTTP_201_CREATED)
def update_task(body :TaskDTO,id : int,db : Session = Depends(get_db),user : UserModel = Depends(is_authenticated)):
    return controller.update_task(body,id,db,user)


# delete task by id
@task_routes.delete("/delete/{id}",response_model= None,status_code= status.HTTP_204_NO_CONTENT)
def delete_task(id : int,db: Session = Depends(get_db),user : UserModel = Depends(is_authenticated)):
    return controller.delete_task(id,db,user) 
