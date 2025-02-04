from fastapi import FastAPI
from src.book.routes import book_router

version = "v1"
app = FastAPI(
    title="Book_Manager",
    description="A REST API for manage book",
    version=version,
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])