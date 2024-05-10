from settlement import Settlement
from fileService import *
from settlementService import *
from typing import *

fileWriteSucceeded: bool = False

# 1
print("Feladat 1:")
settlements:List[Settlement] = getSettlementsFromFile("./adatok.txt")
writeSettlementsToConsole(settlements)

# 2
print("\nFeladat 2:")
settlementsByCountyType:List[Settlement] = getSettlementsByCountyType(settlements, "megyesz�khely megyei jog� v�ros")
fileWriteSucceeded = writeSettlementsToFile("./megyejoguSettlement.txt", settlementsByCountyType)
printFileResultToConsole("megyejoguSettlement.txt", fileWriteSucceeded)

# 3
print("\nFeladat 3:")
settlementsWherePopulationsIsBetween:List[Settlement] = getSettlementsWherePopulationsIsBetween(settlements, 50000, 100000)
fileWriteSucceeded = writeSettlementsToFile("./nepesseg.txt", settlementsWherePopulationsIsBetween)
printFileResultToConsole("nepesseg.txt", fileWriteSucceeded)

# 4
print("\nFeladat 4:")
settlementWithAreOver:List[Settlement] = getSettlementWithAreOver(200, settlements)
fileWriteSucceeded = writeSettlementsToFile("./nagyteruletek.txt", settlementWithAreOver)
printFileResultToConsole("nagyteruletek.txt", fileWriteSucceeded)

# 5
print("\nFeladat 5:")
settlementsOfCounty:List[Settlement] = getSettlementsOfCounty("B�k�s", settlements)
fileWriteSucceeded = writeSettlementsToFile("./bekes.txt", settlementsOfCounty)
printFileResultToConsole("bekes.txt", fileWriteSucceeded)

# 6
print("\nFeladat 6:")
countyNamesWithAreaSize: Dict[str, float] = getCountyNamesWithAreaSize(settlements)
fileWriteSucceeded = writeSettlementsByAreaSize("./megyeterületek.txt", countyNamesWithAreaSize)
printFileResultToConsole("megyeterületek.txt", fileWriteSucceeded)
