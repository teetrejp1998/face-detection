from utils.db_object import db
from utils.const import TESTING, TEST_DB_URL

async def execute(query,is_many, values=None):
    # if TESTING:
    #     await db.connect()
    if is_many:
        await db.execute_many(query=query,values=values)
    else:
        await db.execute(query=query,values=values)
    # if TESTING:
    #     await db.disconnect()

async def fetch(query,is_one,values=None):

    # if TESTING:
    #     await db.connect()
    if is_one:
        result = await db.fetch_one(query=query,values=values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        # print('yoyo')
        result = await db.fetch_all(query=query,values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                # print(dict(row))
                out.append(dict(row))
    # if TESTING:
    #     await db.disconnect()
    # print(result)
    return out


# from datetime import datetime
# query = """select * from attendances where date=:date"""
# values={"date":datetime.now()}