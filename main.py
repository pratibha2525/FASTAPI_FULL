from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1','2'}}

# Class
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



# POST
@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)