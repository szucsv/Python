from student import Student
from typing import *

def printStudentsToConsole(students: List[Student]) -> None:
    for student in students:
        print(student)

def getStudentsAvarageSum(students: List[Student]) -> float:
    avarageSum: float = 0

    for student in students:
        avarageSum += student.avarage

    return avarageSum

def getStudentsAvarage(students: List[Student]) -> float:
    avarageSum: float = getStudentsAvarageSum(students)
    return avarageSum / len(students)

def getHighestAvarage(students: List[Student]) -> float:
    max: float = students[0].avarage

    for index in range(1, len(students), 1):
        if(students[index].avarage > max):
            max = students[index].avarage

    return max

def getBestStudents(students: List[Student]) -> List[Student]:
    bestStudents:List[Student] = []
    maxAvarage: float = getHighestAvarage(students)

    for student in students:
        if(student.avarage == maxAvarage):
            bestStudents.append(student)

    return bestStudents

def getStudentsAboveAvarage(students: List[Student], avarage: float) -> List[Student]:
    studentsAboveAvarage: List[Student] = []

    for student in students:
        if(student.avarage > avarage):
            studentsAboveAvarage.append(student)

    return studentsAboveAvarage

def isAnyExcellentStudent(students: List[Student]) -> bool:
    isAny: bool = False
    
    for student in students:
        if(student.avarage == 5):
            isAny = True
            break
        
    return isAny

def getStudentCategoriesCount(students: List[Student]) -> Dict[str, int]:
    categories: Dict[str, int] = {
        "elégtelen": 0,
        "elégséges": 0,
        "jó": 0,
        "jeles": 0,
        "kitünő": 0,
    }

    for student in students:
        studentCategory: str = student.getCategory()

        #categories[studentCategory] a kulcshoz tartozo erteket adja vissza
        categories[studentCategory] += 1 

    return categories

def printStudentCategoriesToConsole(studentCategories: Dict[str, int]) -> None:
    #key -> str, value -> int resze a szotarnak
    for key, value in studentCategories.items(): 
        print(f"\t - {key} : {value}")