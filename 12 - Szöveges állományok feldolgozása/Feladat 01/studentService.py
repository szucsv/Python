from student import Student
from typing import *


def printStudentsToConsole(students:List[Student]) -> None:
    for student in students:
        print(student)

def getStudentsSum(students:List[Student]) -> float:
    avarageSum:float = 0

    for student in students:
        avarageSum+= student.avarage

    return avarageSum

def getStudentsAvarage(students:List[Student]) -> float:
    avarageSum:float = getStudentsSum(students)

    return avarageSum / len(students)

def getHighestAvarage(students:List[Student])->float:
    max:float=students[0].avarage

    for index in range(1,len(students,1)):
        if(students[index].avarage>max):
            max=students[index].avarage

    return max

def getBestStudents(students:List[Student])->List[Student]:
    bestStudents:List[Student]=[]
    maxAvarage:float=getHighestAvarage(students)

    for student in students:
        if(student.avarage ==maxAvarage):
            bestStudents.append(student)

    return bestStudents

def getStudentsAboveAvarage(students:List[Student],avarage:float)->List[Student]:
    studentsAboveAvarage:List[Student]=[]
    
    for student in students:
        if(student.avarage>avarage):
            studentsAboveAvarage.append(student)



    return studentsAboveAvarage

def isAnyExcellentStudent(students:List[Student])->bool:
    for student in students:
        if(student.avarage==5):
            isAny= True
            break
    
    return False

def getGradesFromStrudents(students: List[Student]) -> Dict[str, int]:
    grades: Dict[str,int] = {}
    oneCounter: int = 0
    twoCounter: int = 0
    threeCounter: int = 0
    fourCounter: int = 0
    fiveCounter: int = 0

    for student in students:
        if(student.avarage >= 0 and student.avarage <= 1.99):
            oneCounter += 1
        elif(student.avarage >= 2 and student.avarage <= 2.99):
            twoCounter += 1
        elif(student.avarage >= 3 and student.avarage <= 3.99):
            threeCounter += 1
        elif(student.avarage >= 4 and student.avarage <= 4.99):
            fourCounter += 1
        else:
            fiveCounter += 1
    
    grades = {"Elégtelen": oneCounter, "Elégséges": twoCounter, "Jó": threeCounter, "Jeles": fourCounter, "Kitűnő": fiveCounter}

    return grades

def getStudentCategoriesCount(students: List[Student])->Dict[str,int]:
    categories:Dict[str,int]={
        "elégtelen":0,
        "elégséges":0,
        "jó":0,
        "jeles":0,
        "kitűnő":0,
    }

    for students in students:
        studentCategory:str=Student.category
        categories[studentCategory]+=1

    return categories

def printStudentCategoriesToConsole(studentCategories:Dict[str,int])->None:
    for key, value in studentCategories.items():
        print(f"\t - {key}:{value}")

