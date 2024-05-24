import datetime
import os
from typing import *

from physicist import Physicist

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getPilotsFromFile(fileName: str) -> List[Physicist]:
    physicists:List[Physicist] = []
    physicist: Physicist = None
    oneLine:str = None
    data: List[str] = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            next(file)
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(";")

                physicist = Physicist()
                physicist.year = int(data[0])
                physicist.type = data[1]
                physicist.firstName = data[2]
                physicist.lastName = data[3]

                physicists.append(physicist)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return physicists

def savePhysicists(fileName: str, physicists: List[Physicist]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for physicist in physicists:
                file.write(f"{physicist.year}:{physicist.getFullName()}")

                if(len(physicists) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False