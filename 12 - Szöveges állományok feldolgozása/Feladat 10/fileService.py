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
     
