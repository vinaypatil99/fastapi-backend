from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.helpers import require_role
from src.users.models import UserModel
from src.tasks.models import TaskModel

admin_routes = APIRouter(prefix="/admin", tags=["Admin"])


# get all users
@admin_routes.get("/users",status_code= status.HTTP_200_OK)
def get_all_users(
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    users = db.query(UserModel).all()

    return {
        "message": "All users fetched successfully",
        "data": users
    }
    
# get all tasks(of all users)
@admin_routes.get("/tasks",status_code= status.HTTP_200_OK)
def get_all_tasks(
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    tasks = db.query(TaskModel).all()

    return {
        "message": "All tasks fetched successfully",
        "data": tasks
    }
    
# get stats
@admin_routes.get("/stats",status_code= status.HTTP_200_OK)
def get_stats(
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):

    users_count = db.query(UserModel).count()
    tasks_count = db.query(TaskModel).count()

    return {
        "total_users": users_count,
        "total_tasks": tasks_count
    }
    
    
# delete user
@admin_routes.delete("/delete/{user_id}",status_code= status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}