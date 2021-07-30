import datetime
from fastapi import Body,Header,File,APIRouter
from models.admin import Admin
from models.attendance import Attendance
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response
from utils.pure_db_function import (
    db_insertAdmin,
    db_checkAdmin,
    db_getAttendanceTime,
    db_insertAttendance)
import re
from utils.security import getHashedPassword
from utils.webcam import saveFaceMarking
from utils.const import IMAGE_PATH
from utils.security import verifyPassword


appV1 = APIRouter()

@appV1.post("/admin",status_code=HTTP_201_CREATED,tags=['user'])
async def postUser(admin:Admin):
    adminObj = dict(admin)
    adminObj['password'] = getHashedPassword(adminObj['password'])
    result_admin = Admin(**adminObj)
    await db_insertAdmin(result_admin)
    return {"result":"Admin is created"}

# query parameter
@appV1.post("/login",tags=['user'])
async def getUserValidation(username:str=Body(...),password:str=Body(...)):
    result = False
    if result:
        if result == "true":
            return {'isValid (redis)':True}
        else:
            return {'isValid (redis)':True}
    else:
        result = await db_checkAdmin(username)
        return {'isValid (db)':verifyPassword(password,result['password'])}

@appV1.get("/attendance/{Date}/att",response_model=Attendance,tags=['attendance'])
async def getAttendanceWithTimestamp(Date:str):
    timeObj = re.split(';|,|:|-',Date)
    year = int(timeObj[0])
    month=int(timeObj[1])
    day=int(timeObj[2])
    Date_ = datetime.date(year,month,day)
    attendance = await db_getAttendanceTime(Date_)
    return attendance

@appV1.post("/photo/{source}",tags=['photo'])
async def uploadUserPhoto(response:Response,source:int):
    response.set_cookie(key="cookie-api",value="test")
    await saveFaceMarking(source=int(source))
    await db_insertAttendance(IMAGE_PATH)
    return {"fileSize": "image uploaded"}


