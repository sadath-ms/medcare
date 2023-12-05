from pydantic import BaseModel

class CreateUser(BaseModel):
    email : str
    password_hash : str

class UserList(BaseModel):
    id : int
    email : str


    

