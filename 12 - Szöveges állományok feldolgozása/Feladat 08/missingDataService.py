from typing import Dict, List, Set

from missingData import MissingData

def getSumOfMissingHours(missingsData:List[MissingData]) -> int:
    sumOfMissingHours: int = 0

    for missingData in missingsData:
        sumOfMissingHours += missingData.missedHours

    return sumOfMissingHours

def hasStudentMissingHours(missingsData:List[MissingData], name: str) -> bool:
    missingHours: int = 0

    for missingData in missingsData:
        if(missingData.name.lower() == name.lower()):
            missingHours = missingData.missedHours

    return missingHours > 0

def getStudentMissingAtDay(studentMissingAtDay:List[MissingData], day: int) -> List[MissingData]:
    studentMissingAtDay:List[MissingData] = []

    for missingData in studentMissingAtDay:
        if(missingData.firstDay >= day and missingData.lastDay <= day):
            studentMissingAtDay.append(missingData)

    return studentMissingAtDay

def printStudentsMissingAtDayToConsole(studentMissingAtDay:List[MissingData], day: int) -> None:
    print(f"\nHianyzok 2017.09.{day}")

    if(len(studentMissingAtDay) == 0):
        print("Nem volt hianyzo")
        return

    for missingData in studentMissingAtDay:
       print(f"{missingData.name} ({missingData.grade})")

def getGrades(missingsData:List[MissingData]) -> Set[str]:
    grades: Set[str] = set()

    for missingData in missingsData:
        grades.add(missingData.grade)

    return grades

def getGroupedMissingHoursForGrades(missingsData:List[MissingData]) -> Dict[str, int]:
    groupedMissingDaysForGrades: Dict[str, int] = {}
    grades: Set[str] = getGrades(missingsData)

    for grade in grades:
        groupedMissingDaysForGrades[grade] = 0

    for missingData in missingsData:
        groupedMissingDaysForGrades[missingData.grade] += missingData.missedHours

    return groupedMissingDaysForGrades
