from typing import *
from io import open
import os
from city import City

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, fileName)


    return fullPath

def getStudentFromFile(fileName: str) -> List[City]:

    cities: List[City] = []
    city: City = None
    oneLine: str = None
    data: List[str] = []

    try:
        fullPath: str = getFileFullPath(fileName)
        with open(fullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split("\t")

                if(data[0] == ""):
                    continue
                
                city = City()
                city.name = data[0]
                city.type = data[1]
                city.county = data[2]
                city.district = data[3]
                city.smallarea = data[4]
                city.population = int(data[5])
                city.zone = float(data[6])

                cities.append(city)

    except FileNotFoundError:
        print(f"{fileName} nem található!")
        exit()

    return cities

def writeCityWithCountryRightsToFile(fileName: str, cityWithCountyRights: List[City]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for city in cityWithCountyRights:
                file.write(f"{str(city)}")
                if(len(cityWithCountyRights) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False

def writePopulationToFile(fileName: str, population: List[City]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for city in population:
                file.write(f"{str(city)}")
                if(len(population) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False

def writeBigAreasToFile(fileName: str, bigAreas: List[City]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for city in bigAreas:
                file.write(f"{str(city)}")
                if(len(bigAreas) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False
    
def writeCitiesInBekesToFile(fileName: str, citiesInBekes: List[City]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for city in citiesInBekes:
                file.write(f"{str(city)}")
                if(len(citiesInBekes) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False
    
def writeCountryAndAreasToFile(fileName: str, countryAndAreas: List[City]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding="utf-8",mode="w+") as file:
            for city in countryAndAreas:
                file.write(f"{str(city)}")
                if(len(countryAndAreas) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError:
        print(f"{fileName} nem található!")

        return False
def writeSettlementbyAreaSize(fileName:str,countryNamesWithAreaSize:Dict[str,float])->Dict[str,float]:
        try:
            filefullPath:str=getFileFullPath(fileName)
            with open(filefullPath,encoding='utf-8',mode="w+")as file:
                for country,areaSize in countryNamesWithAreaSize.items():
                    file.write(f"{country}:{areaSize}m2\n")
            
            return True
        except FileNotFoundError as ex:
            print(f"{ex.fileName}nem talalhato!")
            return False

