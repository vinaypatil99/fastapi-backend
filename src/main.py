from src.utils.db import Base,engine
from src.tasks.router import task_routes
from src.users.router import user_routes
from src.admin.router import admin_routes
from fastapi import FastAPI, HTTPException
from src.utils.exception_handler import http_exception_handler

Base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")
app.include_router(task_routes)
app.include_router(user_routes)
app.include_router(admin_routes)
app.add_exception_handler(HTTPException, http_exception_handler)

