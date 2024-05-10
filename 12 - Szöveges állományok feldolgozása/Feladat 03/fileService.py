import os
from typing import *
from book import Book
from author import Author


def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getBooksFromFile(fileName: str) -> List[Book]:
    books:List[Book] = []
    oneLine:str = None
    data: List[str] = None
    author: Author = None
    book: Book = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")

                author = Author()
                author.firstName = data[0]
                author.lastName = data[1]
                author.birthday = data[2]
                author.honorar = f"${data[10]}"

                book = Book()
                book.author = author
                book.title = data[3]
                book.isbn = data[4]
                book.publisher = data[5]
                book.publishYear = int(data[6])
                book.price = float(data[7])
                book.theme = data[8]
                book.pages = data[9]

                books.append(book)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return books

def writeBooksToFile(fileName: str, books:List[Book]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="a") as file:
            for book in books:
                file.write(str(book))

                if(len(books) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False

def writeBooksByThemeToFile(fileName: str, groupedBooksByTheme: Dict[str, List[Book]]) -> bool:
    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="a") as file:
            for theme, books in groupedBooksByTheme.items():
                file.write(f"{theme}:\n")

                for book in books:
                    file.write(f"\t- {str(book.title)}:\n")

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False