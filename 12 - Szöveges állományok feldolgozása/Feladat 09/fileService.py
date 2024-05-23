import datetime
import os
from typing import *

from freight import Freight

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getFreightsFromFile(fileName: str) -> List[Freight]:
    freights:List[Freight] = []
    freight: Freight = None
    oneLine:str = None
    data: List[str] = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            next(file)
            for line in file:

                oneLine = line.strip()
                data = oneLine.split(";")

                freight = Freight()
                freight.id = int(data[0])
                freight.timeOfDeparture = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
                freight.travelTime = int(data[2])
                freight.distance = float(data[3].replace(",","."))
                freight.fare = float(data[4].replace(",","."))
                freight.tip = float(data[5].replace(",","."))
                freight.paymentType = data[6]

                freights.append(freight)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return freights

def saveFreightsWithError(fileName: str, freights: List[Freight]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            file.write("taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja\n")
            for freight in freights:
                timeOfDeparture: str = freight.timeOfDeparture.strftime("%m/%d/%Y, %H:%M:%S")
                file.write(f"{freight.id};{timeOfDeparture};{freight.travelTime};{freight.distance};{freight.fare};{freight.tip};{freight.paymentType}")

                if(len(freights) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False
    