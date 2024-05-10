from typing import *

class Book:
    def __init__(self):
        self.secondmane: str = None
        self.firstmane: str = None
        self.birthdate: str = None
        self.title: str = None
        self.isbn: str = None
        self.publisher: str = None
        self.date: int = None
        self.price: int = None
        self.theme: str = None
        self.page: int = None
        self.fee: int = None

    def __str__(self) -> str:

        return f"{self.secondmane} {self.firstmane} {self.birthdate} {self.title} {self.isbn} {self.publisher} {self.date} {self.price} {self.theme} {self.page} {self.fee}"