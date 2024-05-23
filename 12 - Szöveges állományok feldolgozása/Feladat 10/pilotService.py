<<<<<<< HEAD
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

=======
from typing import List, Set

from pilot import Pilot


def getPilotsBornBeforeCentury(pilots:List[Pilot], century: int) -> List[Pilot]:
    pilotsBornBeforeCentury: List[Pilot] = []

    startYear: int = ((century - 1) * 100) + 1
    endYear: int = century * 100

    for pilot in pilots:
        if(pilot.birtdate.year >= startYear and pilot.birtdate.year <= endYear):
            pilotsBornBeforeCentury.append(pilot)

    return pilotsBornBeforeCentury

def printPilotsBornBeforeCentury(pilots:List[Pilot]) -> None:
    for pilot in pilots:
        print(f"\t{pilot.name} ({pilot.birtdate.year}. {pilot.birtdate.month}. {pilot.birtdate.day})") 

def getPilotWithTheLowerStartingNumber(pilots:List[Pilot]) -> Pilot:
    pilotWithTheLowerStartingNumber: Pilot = pilots[0]

    for index in range(1, len(pilots), 1):
        if(pilots[index].startNumber == None):
            continue
        elif(pilots[index].startNumber < pilotWithTheLowerStartingNumber.startNumber):
            pilotWithTheLowerStartingNumber = pilots[index]

    return pilotWithTheLowerStartingNumber

def getAllStartingNumbers(pilots:List[Pilot]) -> List[int]:
    stratingNumbers: List[int] = []

    for pilot in pilots:
        if(pilot.startNumber == None):
            continue

        stratingNumbers.append(pilot.startNumber)

    return stratingNumbers

def getMultiplyTimesUsedStartingNumber(pilots:List[Pilot]) -> List[int]:
    stratingNumbers: List[int] = getAllStartingNumbers(pilots)
    seenStartNumbers: Set[int] = set()

    for pilot in pilots:
        if(pilot.startNumber == None):
            continue

        count: int = stratingNumbers.count(pilot.startNumber)
        if(count > 1):
            seenStartNumbers.add(pilot.startNumber)

    return seenStartNumbers
>>>>>>> 012d0f9b88d5e22b861ced892eb512ee28d60415
