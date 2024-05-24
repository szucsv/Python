import datetime
from typing import*

class Nobel:
    def __init__(self) -> None:
        self.year:int=None
        self.type:str=None
        self.surname:str=None
        self.firstName:str=None

    def __str__(self) -> str:
        return f"{self.year}{self.type}{self.surname}{self.firstName}"

