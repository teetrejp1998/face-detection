from datetime import datetime,date
from fastapi import Body,Header,File,APIRouter
from models.admin import Admin
from models.attendance import Attendance
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response
from utils.db_function import (db_insertAdmin,db_checkAdmin,db_getAttendanceTime)
import re

appV1 = APIRouter()
# appV1 = APIRouter()

@appV1.post("/user",status_code=HTTP_201_CREATED,tags=['user'])
async def postUser(user:Admin):
    await db_insertAdmin(user)
    return {"result":"Admin is created"}

# query parameter
@appV1.post("/login",tags=['user'])
async def getUserValidation(username:str=Body(...),password:str=Body(...)):
    redis_key=f"{username},{password}"
    # result = await re.redis.get(redis_key)
    result = False
    if result:
        if result == "true":
            return {'isValid (redis)':True}
        else:
            return {'isValid (redis)':True}
    else:
        result = await db_checkAdmin(username,password)
        # await re.redis.set(redis_key,str(result))
    # print(result)
        return {'isValid (db)':result}

@appV1.get("/attendance/{Datetime}",response_model=Attendance,tags=['attendance'])
async def getAttendanceWithTimestamp(Date:str):
    timeObj = re.split(';|,|:|-',Date)
    Date = date(int(timeObj[0]),int(timeObj[1],int(timeObj[2])))
    attendance = await db_getAttendanceTime(Date)
    result_attendance = Attendance(**attendance)
    return result_attendance
@appV1.post("/user/photo",tags=['user'])
async def uploadUserPhoto(response:Response,profilePhoto: bytes=File(...),):
    response.headers['x-file-size'] = str(len(profilePhoto))
    response.set_cookie(key="cookie-api",value="test")
    
    return {"fileSize":len(profilePhoto)}
