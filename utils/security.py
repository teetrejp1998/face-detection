from passlib.context import CryptContext
from models.jwtUser import JWTUser
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_ALGORITH,JWT_SECRET_KEY
import jwt
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
import time
from utils.db_function import db_checkTokenUser,db_checkJWTUsername
from starlette.status import HTTP_401_UNAUTHORIZED

pwd_context = CryptContext(schemes=['bcrypt'])
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")

def getHashedPassword(password):
    return pwd_context.hash(password)
def verifyPassword(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password,hashed_password)
    except Exception as e:
        return False
# Authenticate username and password to give JWT toker
async def authenticateUser(user:JWTUser):
    potential_users = await db_checkTokenUser(user)
    isValid = False
    for db_user in potential_users:
        if verifyPassword(user.password,db_user['password']):
            isValid=True
    if isValid:
        user.role = "admin"
        return user
    return None
#  Create access JWT token
def createJWTToken(user:JWTUser):
    expiration = datetime.utcnow()+timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwtPayload = {
        "sub":user.username,
        "role":user.role,
        "exp":expiration
    }
    jwtToken = jwt.encode(jwtPayload,JWT_SECRET_KEY,algorithm= JWT_ALGORITH)
    return jwtToken

# Check whether JWT token is correct
async def checkJWTToken(token:str=Depends(oauth_schema)):
    print(token)
    try:
        jwtPayload = jwt.decode(token, JWT_SECRET_KEY,algorithms=JWT_ALGORITH)
        username = jwtPayload.get('sub')
        role = jwtPayload.get('role')
        expiration = jwtPayload.get('exp')
        if time.time()<expiration:
            isValid = db_checkJWTUsername(username)
            if isValid:
                return finalChecks(role)
    except Exception as e:
        # return False
        raise  HTTPException(status_code =HTTP_401_UNAUTHORIZED)
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    # raise False



# Last checking and returning the final result
def finalChecks(role:str):
    if role=="admin":
        return True
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
        # return False

