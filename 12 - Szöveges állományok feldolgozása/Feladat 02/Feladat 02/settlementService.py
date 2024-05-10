import os
from typing import *
from settlement import Settlement

def printFileResultToConsole(fileName: str, fileWriteSucceeded: bool) -> None:
    if(fileWriteSucceeded):
        print(f"{fileName} allomany letrehozva")
    else:
        print(f"{fileName}allomany nem lett letrehozva")

def writeSettlementsToConsole(settlemens:List[Settlement]) -> None:
    for settlement in settlemens:
        print(str(settlement))

def getSettlementsByCountyType(settlemens:List[Settlement], countyType: str) -> List[Settlement]:
        countySettlements:List[Settlement] = []

        for settlement in settlemens:
            if(settlement.type == countyType):
                countySettlements.append(Settlement)
    
        return countySettlements

def getSettlementsWherePopulationsIsBetween(settlements:List[Settlement], min: int, max: int) -> List[Settlement]:
    settlementsWherePopulationsIsBetween:List[Settlement] = []

    for settlement in settlements:
        if(settlement.population >= min and settlement.population <= max):
            settlementsWherePopulationsIsBetween.append(settlement)
    
    return settlementsWherePopulationsIsBetween

def getSettlementWithAreOver(asrea: float, settlements:List[Settlement]) -> List[Settlement]:
    settlements:List[Settlement] = []

    for settlement in settlements:
        if(settlement.area > asrea):
            settlements.append(settlement)

    return settlements

def getSettlementsOfCounty(countyName: str, settlements:List[Settlement]) -> List[Settlement]:
    settlementsOfCounty:List[Settlement] = []

    for settlement in settlements:
        if(settlement.county == countyName):
            settlementsOfCounty.append(Settlement)

    return settlementsOfCounty
 
def getCountyNames(settlements:List[Settlement]) -> Set[str]:
    counties:Set[str] = set()

    for settlement in settlements:
        counties.add(settlement.county)

    return counties

def getCountyNamesWithAreaSize(settlements:List[Settlement]) -> Dict[str, float]:
    countyNamesWithAreaSize: Dict[str, float] = {}

    counties:Set[str] = getCountyNames(settlements)
    for county in counties:
        countyNamesWithAreaSize[county] = 0

    for settlement in settlements:
        countyNamesWithAreaSize[settlement.county] += settlement.area
    
    return countyNamesWithAreaSize