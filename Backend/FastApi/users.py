from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Start the server: uvicorn users:app --reload

# User entity

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Juan", surname="Gonzalez", url="https://github.com/JuanAndresGonzalez", age=25),
         User(id=2, name="Sofia", surname="Latorre",url="https://sofia.com", age=23),
         User(id=3, name="Dante", surname="Latorre",url="https://dante.com", age=4)]

@app.get("/usersjson")
async def usersjson():
    return [{"id":1,"name":"Juan", "surname":"Gonzalez","url":"https://github.com/JuanAndresGonzalez","age":25},
            {"id":2,"name":"Sofia", "surname":"Latorre","url":"https://sofia.com","age":23},
            {"id":3,"name":"Dante", "surname":"Latorre","url":"https://dante.com","age":4}]

@app.get("/users")
async def users():
    return users_list

#Path

@app.get("/user/{id}")
async def user(id: int):
    users = list(filter(lambda user: user.id == id, users_list))
    try:
        return list(users)[0]
    except:
        return {"error":"User not found"}
    
# Query

@app.get("/user/")
async def user(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user:User):
    if type(search_user(user.id))==User:
        return {"error":"The user already exists"}
    else:
        users_list.append(user)
        return{"message":"User successfully added","user":user}
    
@app.put("/user/")
async def user(user:User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return {"message":"User successfully updated","user":user}

    if not found:
        return {"error":"User has not been updated"}
    
@app.delete("/user/{id}")
async def user(id:int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"message":"User successfully deleted"}
    if not found:
        return {"error":"The user has not been deleted"}
    
def search_user(id:int):
    users = list(filter(lambda user: user.id == id, users_list))
    try:
        return list(users)[0]
    except:
        return {"error":"User not found"}
    
