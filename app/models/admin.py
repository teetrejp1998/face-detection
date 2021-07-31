from pydantic import BaseModel
from enum import Enum
from fastapi import Query

class Role(str,Enum):
    admin="admin"

class Admin(BaseModel):
    username:str
    password:str
    mail:str = Query(...,regex="^([a-zA-Z0-9 \-\.]+)@([a-zA-Z0-9 \-\.]+)\.([a-zA-Z]{2,5})$")
    role:Role