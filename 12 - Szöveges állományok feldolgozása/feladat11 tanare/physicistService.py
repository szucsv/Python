from typing import *

from physicist import Physicist

def printPhysicistOnConsole(physicists:List[Physicist]) -> None:
    for physicist in physicists:
        print(f"\t{str(physicist)}")

def getPrizeTypeForPhysicistByName(physicists:List[Physicist], physicistName: str) -> str:
    subject: str = None

    for physicist in physicists:
        if(physicist.getFullName() == physicistName):
            subject = physicist.type
            break

    return  subject

def getWinnerNameForYear(physicists:List[Physicist], year: int, type: str) -> str:
    name: str = None

    for physicist in physicists:
        if(physicist.year == year and physicist.type.lower() == type.lower()):
            name = physicist.getFullName()
            break

    return name

def getWinningOrganisationsFromYear(physicists:List[Physicist], year: int, type:str) -> str:
    winningOrganisations:List[Physicist] = []

    for physicist in physicists:
        if(physicist.year >= year and physicist.lastName == "" and physicist.type.lower() == type.lower()):
            winningOrganisations.append(physicist)

    return  winningOrganisations

def getCurieFamilyWons(physicists:List[Physicist], year) -> str:
    curieFamilyWons:List[Physicist] = []

    for physicist in physicists:
        if("Curie" in physicist.lastName):
            curieFamilyWons.append(physicist)

    return  curieFamilyWons

def getUniquePrizeTypes(physicists:List[Physicist]) -> Set[str]:
    uniquePrizeTypes: Set[str] = set()

    for physicist in physicists:
        uniquePrizeTypes.add(physicist.type)

    return uniquePrizeTypes


def getPrizeCountByTypes(physicists:List[Physicist]) -> Dict[str, int]:
    prizeCountByTypes: Dict[str, int] = {}
    uniquePrizeTypes: Set[str] = getUniquePrizeTypes(physicists)

    for prizeType in uniquePrizeTypes:
        prizeCountByTypes[prizeType] = 0

    for physicist in physicists:
        prizeCountByTypes[physicist.type] += 1

    return prizeCountByTypes

def printPrizeCountByTypes(prizeCountByTypes: Dict[str, int]) -> None:
    for type, count in prizeCountByTypes.items():
        print(f"\t{type}\t\t{count} db")

def orderWonsByYearAscending(physicists:List[Physicist]) -> None:
    temp: Physicist = None

    for i in range(0, len(physicists) - 1, 1):
        for j in range(i + 1, len(physicists), 1):
            if(physicists[j].year < physicists[i].year):
                temp = physicists[i].year
                physicists[i].year = physicists[j].year
                physicists[j].year = temp

def getWonsForPrizeType(physicists:List[Physicist], prizeType: str) -> List[Physicist]:
    prizeTypeWons:List[Physicist] = []

    prizeTypes: Set[str] = getUniquePrizeTypes(physicists)

    if(prizeType.lower() not in prizeTypes):
        raise Exception(f"{prizeType.lower()} tipusu dij nem letezik!")

    for physicist in physicists:
        if(physicist.type.lower() == prizeType.lower()):
            prizeTypeWons.append(physicist)

    orderWonsByYearAscending(prizeTypeWons)

    return prizeTypeWons