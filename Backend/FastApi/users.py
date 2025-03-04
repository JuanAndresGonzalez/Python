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
    return [{"name":"Juan", "surname":"Gonzalez","url":"https://github.com/JuanAndresGonzalez","age":25},
            {"name":"Sofia", "surname":"Latorre","url":"https://sofia.com","age":23},
            {"name":"Dante", "surname":"Latorre","url":"https://dante.com","age":4}]

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
        return {"error":"No se ha encontrado el usuario"}
    
# Query

@app.get("/user/")
async def user(id: int):
    return search_user(id)
    
def search_user(id:int):
    users = list(filter(lambda user: user.id == id, users_list))
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}