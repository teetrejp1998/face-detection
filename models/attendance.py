from pydantic import BaseModel
from datetime import datetime,date
from typing import List

class Attendance(BaseModel):
    id:int
    image:str
    date:date
