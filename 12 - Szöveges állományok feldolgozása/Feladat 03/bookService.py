from typing import *
from book import Book

def writeBooksToConsole(books:List[Book]) -> None:
    for book in books:
        print(str(book))

def getBooksOfTheme(books:List[Book], theme: str) -> List[Book]:
    booksOfTheme:List[Book] = []

    for book in books:
        if(book.theme == theme):
            booksOfTheme.append(book)

    return booksOfTheme
    
def getBooksInCentury(books:List[Book], century: int) -> List[Book]:
    booksInCentury:List[Book] = []
    startYear: int = century * 100    
    endYear: int = (century * 100) + 100

    for book in books:
        if(book.publishYear >= startYear and book.publishYear < endYear):
            booksInCentury.append(book)
    
    return booksInCentury
    
def orderBooksByPageNumbers(books:List[Book]) -> None:
    temp:Book = None

    for i in range(0, len(books), 1):
        for j in range(i + 1, len(books), 1):
            if(books[i].pages > books[j].pages):
                temp = books[j]
                books[j] = books[i]
                books[i] = temp
    
def getBookThemes(books:List[Book]) -> Set[str]:
    themes: Set[str] = set() 

    for book in books:
        themes.add(book.theme)

    return themes

def getGroupedBooksByTheme(books:List[Book]) -> Dict[str, List[Book]]:
    groupedBooksByTheme:Dict[str, List[Book]] = {}
    
    themes:Set[str] = getBookThemes(books)
    for theme in themes:
        groupedBooksByTheme[theme] = []
    
    for book in books:
        groupedBooksByTheme[book.theme].append(book)

    return groupedBooksByTheme

