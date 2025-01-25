# from fastapi import FastAPI, Header
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()


# @app.get('/')
# async def read_root():
#     return {"message":"Hello World"}

# @app.get('/greet')
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message":f"Hello {name}","age": age}

# class BookCreateModel(BaseModel):
#     tittle: str
#     author: str

# @app.post('/create_book')
# async def create_book(book_data:BookCreateModel):
#     return{
#         "tittle":book_data.tittle,
#         "author":book_data.author
#     }

# @app.get('/get_headers',status_code=201)
# async def get_headers(
#     accept: str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     request_header ={}
#     request_header["Accept"] = accept
#     request_header["Content-Type"] = content_type
#     request_header["User-Agent"] = user_agent
#     request_header["Host"] = host
#     return request_header

'''
    new test
'''
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English"
    }
]

class Book(BaseModel):
        id: int
        title: str
        author: str
        publisher: str
        published_date: str
        page_count: int
        language: str

class BookUpdateModel(BaseModel):
        title: str
        author: str
        publisher: str
        page_count: int
        language: str

@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)

    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch('/books/{book_id}')
async def update_book(book_id:int, book_update:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publisher'] = book_update.publisher
            book['page_count'] = book_update.page_count
            book['language'] = book_update.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete('/books/{book_id}')
async def delete_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")