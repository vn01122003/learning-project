from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message":"Hello World"}

@app.get('/greet')
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message":f"Hello {name}","age": age}

class BookCreateModel(BaseModel):
    tittle: str
    author: str

@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return{
        "tittle":book_data.tittle,
        "author":book_data.author
    }