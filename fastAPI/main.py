from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()    # Create an instance of the FastAPI

class Custom(BaseModel):
    name: str
    age: int

# The app instance is the main component of FASTAPI application used to configure the application
@app.get('/ping') # ping is the route... 
async def root():
    return {"message" : "Hello World"}

@app.get('/')
async def root():
    return {"message" : "welcome to home page"}

@app.post('/blog/{blog_id}')         
async def root(blog_id: int, request_body:Custom, first_name: str = None, last_name: str = None): # 1. path param 2. request body 3 & 4. query params
    print(request_body)
    print(blog_id, first_name, last_name)
    return {"Blog id": blog_id, "first_name": first_name, "last_name": last_name}