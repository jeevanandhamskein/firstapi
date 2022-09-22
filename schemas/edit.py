#from unicodedata import name
from pydantic import BaseModel

class edit_val(BaseModel):
    name:str
    email:str
    password:str