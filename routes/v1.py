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
import utils.redisObject as redi
from typing import Dict,List,Tuple,Set


appV1 = APIRouter()

@appV1.post("/admin",status_code=HTTP_201_CREATED,tags=['admin'])
async def postUser(admin:Admin):
    adminObj = dict(admin)
    adminObj['password'] = getHashedPassword(adminObj['password'])
    result_admin = Admin(**adminObj)
    await db_insertAdmin(result_admin)
    return {"result":"Admin is created"}

# query parameter
@appV1.post("/login",tags=['admin login'])
async def getUserValidation(username:str=Body(...),password:str=Body(...)):
    admin = await db_checkAdmin(username)
    hash_pass = admin['password']
    redis_key = f"{username},{hash_pass}"
    result = await redi.redis.get(redis_key)
    # redis has the data
    if result:
        if result.decode("utf-8") == "true":
            return {'isValid (redis)':True}
        else:
            return {'isValid (redis)':False}
    # redis does not has the data
    else:
        result = verifyPassword(password,hash_pass)
        print(str(result))
        await redi.redis.set(redis_key,str(result).lower(),expire=10)
        return {'isValid (db)':verifyPassword(password,hash_pass)}

@appV1.get("/attendance/",response_model=List[Attendance],tags=['attendance'])
async def getAttendance():
    attendance = await db_getAttendanceTime()
    return attendance

@appV1.post("/photo/{source}",tags=['photo'])
async def uploadUserPhoto(response:Response,source:int=None,rtsp:str=None):
    response.set_cookie(key="cookie-api",value="test")
    if not(rtsp is None) or not(source is None):
        if rtsp is None:
            await saveFaceMarking(source=int(source))
        if source is None:
            await saveFaceMarking(source=rtsp)
        await db_insertAttendance(IMAGE_PATH)
        return {"fileSize": "image uploaded"}
    else:
        return {"msg":"no source"}


