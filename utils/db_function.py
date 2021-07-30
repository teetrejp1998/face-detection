from utils.db import fetch,execute
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
    values(:name, :password, :mail, :role)"""
    values = dict(admin)
    # print(values)

    await execute(query=query, is_many=False, values=values)

async def db_insertAttendance(image):
    query = """insert into attendances(image, date )
    values(:image, :date)"""
    values = {"image":image,"date":datetime.now()}
    # print(values)

    await execute(query=query, is_many=False, values=values )

async def db_getAttendanceTime(timestamp):
    query = """select * from attendances where timestamp=:timestamp"""
    values={"timestamp":timestamp}
    all_timestamp = await fetch(query,True, values)
    return all_timestamp

async def db_checkAdmin(username,password):
    query = """select * from admins where username = :username and password = :password"""
    values = {"username":username,"password":password}
    result = await fetch(query, True, values)
    if result is None:
        return False
    else:
        return True
