from fastapi import APIRouter, Depends, Query,status,HTTPException
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.security import require_role
from src.users.models import UserModel
from src.tasks.models import TaskModel
from src.utils.helpers import pagination

admin_routes = APIRouter(prefix="/admin", tags=["Admin"])


# get all users
@admin_routes.get("/users", status_code=status.HTTP_200_OK)
def get_all_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    query = db.query(UserModel)

    result = pagination(query, page, limit)

    return {
        "message": "All users fetched successfully",
        **result
    }
    
    
# get all tasks(of all users)
@admin_routes.get("/tasks", status_code=status.HTTP_200_OK)
def get_all_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    query = db.query(TaskModel)

    result = pagination(query, page, limit)

    return {
        "message": "All tasks fetched successfully",
        **result
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
        raise HTTPException(status_code=404, detail="User not found!!")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}