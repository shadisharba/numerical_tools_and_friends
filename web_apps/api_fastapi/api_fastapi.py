"""
There are 5 popular HTTP methods, namely GET, POST, PUT, PATCH, and DELETE which can be used to manage the state of resources.

GET: Retrieve an existing resource (read-only)
POST: Create a new resource
PUT: Update an existing resource
PATCH: Partially update an existing resource
DELETE: Delete a resource
"""

from fastapi import FastAPI
from pydantic import BaseModel

# 1. Define an API object
app = FastAPI()


# 2. Define data type
class Msg(BaseModel):
    msg: str


# 3. Map HTTP method and path to python function
@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the API home page!"}


@app.get("/path")
async def function_demo_get():
    return {"message": "This is /path endpoint, use post request to transform text to uppercase"}


@app.post("/path")
async def function_demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def function_demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
