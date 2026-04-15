from src.tasks.dtos import TaskDTO
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.users.models import UserModel
from fastapi import HTTPException


def create_task(body : TaskDTO,db : Session,user : UserModel):
    data = body.model_dump()
    
    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"],
        user_id = user.id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task


def get_all_tasks(db : Session,user : UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks


def get_by_id(id : int,db : Session):
    task = db.query(TaskModel).get(id)
    
    if not task:
        raise HTTPException(404,detail= "task not found!!")
    
    return task


def update_task(body : TaskDTO,id : int,db : Session,user : UserModel):
    task = db.query(TaskModel).get(id)
    
    if not task:
        raise HTTPException(404,detail= "task not found!!")
    
    if task.user_id != user.id :
        raise HTTPException(401,detail= "You cannot edit this task!!")
        
    
    body = body.model_dump()
    for field,value in body.items():
         setattr(task,field,value)
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task


def delete_task(id : int,db : Session,user : UserModel):
    task = db.query(TaskModel).get(id)
    
    if not task:
        raise HTTPException(404,detail= "task not found!!")
    
    if task.user_id != user.id :
        raise HTTPException(401,detail= "You cannot delete this task!!")    
    
    db.delete(task)
    db.commit()
    
    return None
    
    