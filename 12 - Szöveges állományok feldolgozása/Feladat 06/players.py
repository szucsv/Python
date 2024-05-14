from typing import *

class players:
    def __init__(self) -> None:
        self.number:int = None
        self.lastName:str=None
        self.surnname:int = None
        self.birthDate:str=None
        self.citizenship:bool = None
        self.noCitizenship:bool=None
        self.value:int = None
        self.clubName:str=None
        self.position:int = None
    
    def __str__(self) -> str:
        return f"{self.number} {self.lastName} {self.surnname} {self.birthDate} {self.citizenship} {self.noCitizenship} {self.value}{self.clubName}{self.position}"
         