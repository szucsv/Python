import random
from typing import List

from fileService import *
from missingDataService import *
from missingData import MissingData


missingsData:List[MissingData] = getMissingDataFromFile("szeptember.csv")

#2
sumOfMissingHours: int = getSumOfMissingHours(missingsData)
print(f"\nOsszes mulasztott orak szama: {sumOfMissingHours}")
    
#3
day: int = random.randint(1, 30)
name: str = missingsData[random.randint(0, len(missingsData) - 1)].name

#4
hasStudentMissingHours: bool = hasStudentMissingHours(missingsData, name)
if(hasStudentMissingHours):
    print(f"\nA {name} hianyzott szeptemberben")
else:
    print(f"\nA {name} nem hianyzott szeptemberben")

#5
studentMissingAtDay:List[MissingData] = getStudentMissingAtDay(missingsData, day)
printStudentsMissingAtDayToConsole(studentMissingAtDay, day)

#6
groupedMissingDaysForGrades: Dict[str, int] = getGroupedMissingHoursForGrades(missingsData)
isFileWriteSucceeded: bool = writeMissedHoursByGrade("osszesites.csv", groupedMissingDaysForGrades)
if(isFileWriteSucceeded):
    print("\nosszesites.csv mentese sikeres")
else:
    print("\nosszesites.csv mentese sikertelen")  
    