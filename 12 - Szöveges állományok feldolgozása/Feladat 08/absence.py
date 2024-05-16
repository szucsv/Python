from typing import *

class Absance:
    def __init__(self) -> None:
        self.name:str=None
        self.grade:str=None
        self.firstDay:None
        self.lastDay:int=None
        self.missedClasses=None

    def __str__(self) -> str:
        return f"{self.name}{self.grade}{self.firstDay}{self.lastDay}{self.missedClasses}"