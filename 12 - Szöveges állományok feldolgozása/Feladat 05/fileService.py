import itertools
import os
from typing import *
from volleyballTeam import VolleyballTeam

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def convertStringCollectionToIntSet(numbersAsStringCollection:str) -> List[int]:
    numbersAsIntCollection: List[int] = []

    for numberAsString in numbersAsStringCollection.replace(", ", ",").split(","):
        if(numberAsString == ""):
            continue

        number: int = int(numberAsString)
        numbersAsIntCollection.append(number)

    return numbersAsIntCollection

def getVolleyballTeamsFromFile(fileName: str) -> List[VolleyballTeam]:
    volleyballTeams:List[VolleyballTeam] = []
    volleyballTeam: VolleyballTeam = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8-sig', mode="r") as file:
            for teamName,teapPoints in itertools.zip_longest(*[file]*2):
                
                volleyballTeam = VolleyballTeam()
                volleyballTeam.name = teamName.strip()
                volleyballTeam.points = convertStringCollectionToIntSet(teapPoints.strip())

                volleyballTeams.append(volleyballTeam)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return volleyballTeams
