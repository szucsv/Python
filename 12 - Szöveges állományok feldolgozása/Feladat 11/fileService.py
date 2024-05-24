from typing import *
from io import open
from nobel import *
import os


def getFileFullPath(fileName:str)->str:
    basePath:str=os.path.dirname(__file__)
    return os.path.join(basePath,fileName)

def nobelFromFile(fileName:str)->List[Nobel]:
    nobel:Nobel=None
    nobels:List[Nobel]=[]
    data:List[str]=[]
    oneLine:str =None

    try:
        fullPath:str=getFileFullPath(fileName)

        with open (fullPath,mode="r",encoding="utf-8")as file:
            next(file)

            for line in file:

                oneLine=line.strip()
                data=oneLine.split(";")
                nobel=Nobel()
                nobel.year=int(data[0])
                nobel.type=data[1]
                nobel.surname=data[2]
                if(data[3]==""):
                    nobel.firstName=""
                else:
                    nobel.firstName=data[3]
                 
                nobels.append(nobel)
    
    except Exception as ex:
        print(f"Hiba:{ex}")

    return nobels