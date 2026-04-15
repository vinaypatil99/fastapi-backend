from pydantic import BaseModel

class UserDTO(BaseModel):
    name : str
    username : str
    password : str
    email : str
    
    
class UserResponseDTO(BaseModel):
    name : str
    username : str
    email : str
    id : int
    

class LoginDTO(BaseModel):
   username : str
   password : str