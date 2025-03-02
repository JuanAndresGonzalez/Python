# Author: Juan Andres Gonzalez

# Official documentation: https://fastapi.tiangolo.com/es/

# Installs FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()

# Local url: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "Hello FastAPI!"

#Local url: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url":"https://github.com/JuanAndresGonzalez"}

# Start the server: uvicorn main:app --reload
# Stop the server: CTRL+C

# Documentation with Swagger: http://127.0.0.1:8000/docs
# Documentation with Redocly: http://127.0.0.1:8000/redoc