import datetime
import os
from typing import *

from pilot import Pilot

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getPilotsFromFile(fileName: str) -> List[Pilot]:
    pilots:List[Pilot] = []
    pilot: Pilot = None
    oneLine:str = None
    data: List[str] = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            next(file)
            for line in file:

                oneLine = line.strip()
                data = oneLine.split(";")

                pilot = Pilot()
                pilot.name = data[0]
                pilot.birtdate = datetime.datetime.strptime(data[1], "%Y.%m.%d")
                pilot.nationality = data[2]
                pilot.startNumber = int(data[3]) if(data[3] != '') else None

                pilots.append(pilot)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return pilots