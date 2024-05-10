from books import *
from fileService import *
from typing import *
from bookService import *

books: List[Book] = getBooksFromFile("adatok.txt")
printToConsole(books)

BooksWIT: List[Book] = getBooksWIT(books)
ITFileSuccess: bool = writeToFile("informatika.txt", BooksWIT)
if(ITFileSuccess):
    print("\ninformatika.txt allomanyban talalja a konyveket")
else:
    print("\ninformatika.txt-t nem sikerult letrehozni")



