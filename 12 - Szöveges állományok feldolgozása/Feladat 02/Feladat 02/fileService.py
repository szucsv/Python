import os
from typing import *
from settlement import Settlement

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getSettlementsFromFile(fileName: str) -> List[Settlement]:
    settlements:List[Settlement] = []
    oneLine:str = None
    data: List[str] = None
    settlement: Settlement = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")

                settlement = Settlement()
                settlement.name = data[0]
                settlement.type = data[1]
                settlement.county = data[2]
                settlement.countyDistrict = data[3]
                settlement.microRegion = data[4]
                settlement.population = int(data[5])
                settlement.area = float(data[6])

                settlements.append(settlement)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return settlements

def writeSettlementsToFile(fileName: str, settlements:List[Settlement]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="a") as file:
            for Settlement in settlements:
                file.write(str(Settlement))

                if(len(settlements) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False

def writeSettlementsByAreaSize(fileName: str, countyNamesWithAreaSize: Dict[str, float]) -> bool:
    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for county, areaSize in countyNamesWithAreaSize.items():
                file.write(f"{county}: {areaSize}m2\n")

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False