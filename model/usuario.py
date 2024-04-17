from pydantic import BaseModel

class Usuario(BaseModel):
    _id : str
    nombre : str
    email : str
    password : str