import asyncio
from starlette.testclient import TestClient
from run import app
from utils.pure_db import fetch,execute
from utils.security import getHashedPassword

client = TestClient(app)
loop = asyncio.get_event_loop()

# def insert_admin(username,password):
#     query = """insert into admins(username,password) values(:username,:password,:mail,:role)"""
#     hash_password = getHashedPassword(password)
#     values = {"username":username,"password":hash_password,"role":"admin","mail":"a@b.com"}
#     loop.run_until_complete(execute(query=query,is_many=False,values=values))

# def clear_db():
#     query1="""delete from admins;"""
#     query2="""delete from attendances;"""
#     loop.reset_all(execute(query=query1,is_many=False,values=None))
#     loop.reset_all(execute(query=query2,is_many=False,values=None))

def test_token_authorized():
    # insert_admin(username="user1",password="pass1")
    response = client.post("/token",files=dict(username='North',password="pass3"))
    print(response.json())
    assert response.status_code == 200
    assert "access token" in response.json()
    # clear_db()

# def test_token_unauthorized():
#     insert_admin(username="user1",password="pass1")
#     response = client.post("/token",files=dict(username='df',password="pass3"))
#     assert response.status_code == 401
#     assert "access token" in response.json()
#     clear_db()