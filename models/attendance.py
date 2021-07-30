from pydantic import BaseModel
from datetime import datetime,date

class Attendance(BaseModel):
    image:str
    date:date