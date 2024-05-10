from fileService import *
from bookService import *
from book import Book
from typing import *

isFileExportSucceeded: bool = False
books:List[Book] = getBooksFromFile("adatok.txt")

# 1
writeBooksToConsole(books)

# 2
ITBooks:List[Book] = getBooksOfTheme(books, "informatika")
isFileExportSucceeded = writeBooksToFile("informatika.txt", ITBooks)
if(isFileExportSucceeded):
    print("\nAz informatika.txt sikeressen letrehozva")
else:
    print("\nAz informatika.txt letrehozasa hibara futott")

# 3
booksOf19Centory:List[Book] = getBooksInCentury(books, 19)
isFileExportSucceeded = writeBooksToFile("1900.txt", booksOf19Centory)
if(isFileExportSucceeded):
    print("\nA 19. szazad konyvei elmentve a 1900.txt allomanyba")
else:
    print("\nA 19. szazad konyveinek mentese nem sikerult a 1900.txt allomanyba")

# 4
orderBooksByPageNumbers(books)
isFileExportSucceeded = writeBooksToFile("sorbarakott.txt", books)
if(isFileExportSucceeded):
    print("\nA sorbarakott.txt allomanyba a konyvek oldal szama szerint novekvo sorrendbe el lettek mentve")
else:
    print("\nA sorbarakott.txt mentese sikertelen volt")

# 5
groupedBooksByTheme:Dict[str, List[Book]] = getGroupedBooksByTheme(books)
isFileExportSucceeded = writeBooksByThemeToFile("kategoriak.txt", groupedBooksByTheme)
if(isFileExportSucceeded):
    print("\nA konyvek tema szerint mentve vannak")
else:
    print("\nA konyvek mentese tema szerint nem sikerult")
