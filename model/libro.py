from pydantic import BaseModel

class Libro(BaseModel):
    _id : str
    titulo : str
    autor : str
    isbn : str