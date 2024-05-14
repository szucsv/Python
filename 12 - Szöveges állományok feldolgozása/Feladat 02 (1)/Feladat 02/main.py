from city import City
from fileService import *
from typing import *
from cityServices import *

cities: List[City] = getStudentFromFile("adatok.txt")

printCitiesToConsole(cities)

cityWithCountyRights: List[City] = getCityWithCountyRights(cities)

ifCountryFileWriteSuccess: bool = writeCityWithCountryRightsToFile("megyejoguvarosok.txt", cityWithCountyRights)

if(ifCountryFileWriteSuccess):
    print("\nmegyejoguvarosok.txt állomány mentése sikeres volt!")
else:
    print("\nmegyejoguvarosok.txt állomány mentése sikertelen volt!")

population: List[City] = getPopulationBetween(cities)

ifPopulationFileWriteSuccess: bool = writePopulationToFile("nepesseg.txt", population)

if(ifPopulationFileWriteSuccess):
    print("\nnepesseg.txt állomány mentése sikeres volt!")
else:
    print("\nnepesseg.txt állomány mentése sikertelen volt!")

bigAreas: List[City] = getBigAreas(cities)

ifBigAreasFileWriteSuccess: bool = writeBigAreasToFile("nagyteruletek.txt", bigAreas)

if(ifPopulationFileWriteSuccess):
    print("\nnagyteruletek.txt állomány mentése sikeres volt!")
else:
    print("\nnagyteruletek.txt állomány mentése sikertelen volt!")

citiesInBekes: List[City] = getCitiesInBekes(cities)

ifCitiesInBekesFileWriteSuccess: bool = writeCitiesInBekesToFile("bekes.txt", citiesInBekes)

if(ifCitiesInBekesFileWriteSuccess):
    print("\nbekes.txt állomány mentése sikeres volt!")
else:
    print("\nbekes.txt állomány mentése sikertelen volt!")

countryAndAreas: List[City] = getCountryAndAreas(cities)

ifCountryAndAreasFileWriteSuccess: bool = writeCountryAndAreasToFile("megyeteruletek.txt", countryAndAreas)

if(ifCountryAndAreasFileWriteSuccess):
    print("\nmegyeteruletek.txt állomány mentése sikeres volt!")
else:
    print("\nmegyeteruletek.txt állomány mentése sikertelen volt!")