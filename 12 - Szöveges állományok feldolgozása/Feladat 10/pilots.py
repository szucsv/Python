from typing import *

class Pilot:
    def __init__(self) -> None:
        self.name:str=None
        self.birthDate:str=None
        self.nationality:str=None
        self.raceNum:int=None
    
    def __str__(self) -> str:
        return f"{self.name} {self.birthDate} {self.nationality} {self.raceNum}"