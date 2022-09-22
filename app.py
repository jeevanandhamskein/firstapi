# import email
# import re
# from unicodedata import name
from fastapi import FastAPI
from config.db import conn
from models.user import users
from schemas.user import User
from schemas.edit import edit_val

#import uvicorn

app = FastAPI()

#app.include_router(user)

@app.get('/')
def helloworld():
    return {"hello world"}


@app.get('/users')
async def get_users(id:int):                             # async= path operation functions
    data=conn.execute(users.select().where(users.c.id==id)).first()
    if data:
        return data
    else:
        return {"data not found"}    


@app.post('/adduser')
async def create_user(user:User):
    new_user = {"id":user.id,"name":user.name,"email":user.email,"password":user.password}
    
    emails=conn.execute(
        users.select().where(users.c.email==user.email)
    ).first()
    if emails:
        return {"email already exist"}

    else:
        conn.execute(users.insert().values(new_user))
        id=conn.execute(
            users.select().where(users.c.email == user.email)
        ).first()
        if id:
            return {"added success"}


@app.put('/update')
async def upd_user(id:int,val:edit_val):           #val is instance,edit_val is class name
    ids=conn.execute(users.select().where(users.c.id==id)).first()
    if ids:
        conn.execute(
            users.update()
            .where(users.c.id==id)           #talename.c(column).id
            .values(name=val.name,email=val.email,password=val.password)
        )
        return {"update successfully"}
    else:
        return {"data not found"}    




@app.delete('/delete')
async def upd_user(id:int):
    ids=conn.execute(users.select().where(users.c.id==id)).first()
    if ids:
        conn.execute(
            users.delete()
            .where(users.c.id==id)
        )
        return {"deleted"}

    else:
        return {"data not found"}


@app.get('/getall')
async def get_users():               
    return conn.execute(users.select()).fetchall()









