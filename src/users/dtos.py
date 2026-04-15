from pydantic import BaseModel
from typing import Optional

class UserDTO(BaseModel):
    name : str
    username : str
    password : str
    email : str
    role: Optional[str] = "user"
    
    
class UserResponseDTO(BaseModel):
    name : str
    username : str
    email : str
    id : int
    

class LoginDTO(BaseModel):
   username : str
   password : str