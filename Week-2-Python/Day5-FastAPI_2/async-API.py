'''
Asynchronous programming means:
When one task is waiting for a database, API, or file python can work on another task instead of sitting idle.
'''

from fastapi import FastAPI
import asyncio


app=FastAPI()

@app.get("/users/{username}")
async def get_user(username:str):
    await asyncio.sleep(3)
    return{
        "message":"Asynchronous API",
        "username":username
    }

@app.post("/users")
async def add_user(username:str,name:str,age:int):
    await asyncio.sleep(1)
    return{
        "message":"User added successfully",
        "username":username,
        "name":name,
        "age":age
        
    }

@app.put("/users/{username}")
async def update_user(username:str,name:str,age:int):
    await asyncio.sleep(2)
    return{
        "message":"User updated successfully",
        "username":username,
        "name":name,
        "age":age
    }
