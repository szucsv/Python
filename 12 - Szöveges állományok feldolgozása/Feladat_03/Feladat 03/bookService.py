from typing import *
from books import *

def printToConsole(books:List[Book]) -> None:
    for Book in books:
        print(Book)

def getBooksWIT(books: List[Book]) -> List[Book]:
    theme: List[Book] = []

    for book in books:
        if(book.theme == "informatika"):
            theme.append(book)

    return theme

def getBooksInCentury(books:List[Book])->List[Book]:
    date:List[Book]=[]

    for book in books:
        if(book.date<2000 and book.date >=1900):
            date.append(book)
    return date
