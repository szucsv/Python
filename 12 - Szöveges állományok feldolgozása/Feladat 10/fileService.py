<<<<<<< HEAD
from typing import *
from pilots import *
from io import open
import os

def getFileFullPath(filename:str)->str:
    basePath:str=os.path.dirname(__file__)
    return os.path.join(basePath,filename)

def getPilotsFromFile(filename:str)->List[Pilot]:
    pilots:List[Pilot]=[]
    pilot:Pilot=None
    oneLine:str=None
    data:List[str]=[]

    try:
        fullPath:str= getFileFullPath(filename)
            
        with open(fullPath,mode="r",encoding="utf-8") as file:
            next(file) 
            for line in file:
                oneLine=line.strip()
                data=oneLine.split(";")
                pilot=Pilot()

                pilot.name=data[0]
                pilot.birthDate=data[1]
                pilot.nationality=data[2]
                if(data[3]!=""):
                    pilot.raceNum=int(data[3])
                else:
                    pilot.raceNum=""

                pilots.append(pilot)

    except Exception as ex:
        print(ex)
    return pilots
     
=======
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
>>>>>>> 012d0f9b88d5e22b861ced892eb512ee28d60415
