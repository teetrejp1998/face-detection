from datetime import datetime
from fastapi import FastAPI,Depends,HTTPException
from models.jwtUser import JWTUser
from routes.v1 import appV1
from starlette.status import HTTP_401_UNAUTHORIZED
from starlette.requests import Request
from utils.security import checkJWTToken
from fastapi.security import OAuth2PasswordRequestForm
from utils.const import TOKEN_DESC,TOKEN_SUMMARY
from utils.db_object import db
from utils.security import (
    authenticateUser,
    createJWTToken,
    checkJWTToken)


app = FastAPI(title="Face API Documentation",description="It is an API using for attendance.",version="1.0.0")

app.include_router(appV1, prefix="/v1", dependencies=[Depends(checkJWTToken)])

@app.on_event("startup")
async def connect_db():
    await db.connect()

@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()

@app.post('/token',summary=TOKEN_SUMMARY,description=TOKEN_DESC)
async def loginForAccessToken(formData:OAuth2PasswordRequestForm=Depends()):
    jwt_user_dict = {
        "username":formData.username,
        "password":formData.password}
    jwt_user = JWTUser(**jwt_user_dict)

    user = await authenticateUser(jwt_user)
    # print(jwt_user)
    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    jwt_token = createJWTToken(user)
    return {"access_token":jwt_token}

@app.middleware('http')
async def middleware(req:Request,call_next):
    start_time = datetime.utcnow()
    res = await call_next(req)
    # modify res
    execution_time = (datetime.utcnow()-start_time).microseconds
    res.headers['x-execution-time'] = str(execution_time)
    return res


