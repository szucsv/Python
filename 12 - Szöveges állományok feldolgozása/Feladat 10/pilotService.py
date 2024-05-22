from pilots import *
from fileService import *
from typing import *


def wasBornIn19(pilots:List[Pilot])->List[str]:
    born:List[str]

    century:int=1900

    for pilot in pilots:
        if(pilot.birthDate[:4]<century):
            born.append(pilot.name)

    return born

def yearAndPilot(pilots:List[Pilot])->Dict[str,str]:
    yearAndPilot:Dict[str,str]={}

    bornIn19:List[str]=wasBornIn19(pilots,born)
    
    for born in bornIn19:
        yearAndPilot[born] = 0
    
    for born in bornIn19:
        yearAndPilot[pilot.name] += pilot.birthDay
    
    return yearAndPilot

def printRecent(yearAndPilot:Dict[str,str])->None:
    for pilot,year in yearAndPilot.items():
        print(f"\t{pilot}({year})")

