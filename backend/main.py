from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.fetch_books import (
    get_popular_books,
    search_books,
    get_book_details,
    get_books_details
)

from recommendation import (recommend_book,search_recommendable_books)

app = FastAPI(
    title="Book Recommendation API",
    description="API for Book Recommendation System",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Book Recommendation API is running successfully!"
    }

#Requesting FastAPI to return popular books
#Using MySQL query from 'fetch_books.py' "get_popular_books" for popular books
@app.get("/popular-books")
def popular_books():
    books = get_popular_books()
    return books

@app.get("/search")
def search(query: str):
    books = search_recommendable_books(query)
    return books

@app.get("/book/{title}")
def book_details(title: str):
    return get_book_details(title)

@app.get("/recommend/{title}")
def recommend(title: str):

    recommended_isbns = recommend_book(title)
    books = get_books_details(recommended_isbns)
    return books