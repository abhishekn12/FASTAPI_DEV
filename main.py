from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get('/')
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def posts():
    return {"data":"Post is retrieved"}

@app.post("/createposts")
def send_post(new_post: Post):
    print(new_post.rating)
    return {"data": "new post"}