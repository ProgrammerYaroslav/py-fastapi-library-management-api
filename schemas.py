from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# --- Book Schemas ---
class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date

class BookCreate(BookBase):
    # We pass author_id explicitly when creating a book via a general endpoint,
    # or handle it in the backend if using a nested route. 
    # Here we will allow passing it in the body for flexibility.
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True

# --- Author Schemas ---
class AuthorBase(BaseModel):
    name: str
    bio: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List[Book] = [] # Nested list of books

    class Config:
        from_attributes = True
