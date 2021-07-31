from utils.pure_db import fetch,execute
from datetime import datetime

async def db_checkTokenUser(admin):
    query = """select * from admins where username = :username"""
    values = {"username":admin.username}
    result = await fetch(query, False, values)
    
    if result is None:
        return None
    else:
        return result

async def db_checkJWTUsername(username):
    query = """select * from admins where username = :username"""
    values = {"username":username}
    result = await fetch(query = query,is_one= True, values=values)
    if result is None:
        return False
    else:
        return True

async def db_insertAdmin(admin):
    query = """insert into admins(username, password, mail, role )
    values(:username, :password, :mail, :role)"""
    values = dict(admin)
    # print(values)

    await execute(query=query, is_many=False, values=values)

async def db_insertAttendance(imageB):
    query = """insert into attendances(image, date )
    values(:image, :date)"""
    values = {"image":imageB,"date":datetime.now()}
    result = await execute(query=query, is_many=False, values=values )
    print(result)

async def db_getAttendanceTime():
    query = """select * from attendances"""
    all_timestamp = await fetch(query=query,is_one=False, values=None)
    # print(all_timestamp)
    return all_timestamp

async def db_checkAdmin(username):
    query = """select * from admins where username = :username """
    values = {"username":username}
    result = await fetch(query = query,is_one= True, values=values)
    return result
    # if result is None:
    #     return False
    # else:
    #     return True