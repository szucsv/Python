from typing import *
from io import *
import os
from books import *

def getFilePath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, fileName)

    return fullPath

def getBooksFromFile(fileName: str) -> List[Book]:

    books: List[Book] = []
    book: Book = None
    Line:str = None
    data: List[str] = []

    fullPath: str = getFilePath(fileName)

    with open(fullPath,encoding='utf-8', mode="r") as file:
            
            for line in file:
                Line = line.strip()

                data = Line.split('\t')

                if(data[0] == ""):
                     continue
                book = Book()
                book.secondmane = data[0]
                book.firstmane = data[1]
                book.birthdate = data[2]
                book.title = data[3]
                book.isbn = data[4]
                book.publisher = data[5]
                book.date = int(data[6])
                book.price = int(data[7])
                book.theme = data[8]
                book.page = int(data[9])
                book.fee = int(data[10])

                books.append(book)



    return books

def writeToFile(fileName: str, input: List[Book]) -> bool:
        fullPath: str = getFilePath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for book in input:
                file.write(f"{str(book)}")
                if(len(input) != index):
                    file.write("\n")

                index += 1

        return True

