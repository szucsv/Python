import os
from typing import *

from missingData import MissingData

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getMissingDataFromFile(fileName: str) -> List[MissingData]:
    missings:List[MissingData] = []
    missing: MissingData = None
    oneLine:str = None
    data: List[str] = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            next(file)
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(";")

                missing = MissingData()
                missing.name = data[0]
                missing.grade = data[1]
                missing.firstDay = int(data[2])
                missing.lastDay = int(data[3])
                missing.missedHours = int(data[4])

                missings.append(missing)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return missings

def writeMissedHoursByGrade(fileName: str, roupedMissingDaysForGrades: Dict[str, int]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for grade, missedHours in roupedMissingDaysForGrades.items():
                file.write(f"{grade};{missedHours}")

                if(len(roupedMissingDaysForGrades) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False