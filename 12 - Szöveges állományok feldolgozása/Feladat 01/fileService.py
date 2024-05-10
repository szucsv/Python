import os
from typing import *
from io import open
from student import Student

def getFileFullPath(fileName:str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    fullPath: str = os.path.join(basePath, fileName)

    return fullPath

def getStutentsFromFile(fileName:str) -> List[Student]:

    students: List[Student] = []
    student: Student = None
    oneLine:str = None
    data:List[str] = []

    try:
        fullPath: str =getFileFullPath(fileName)
        
        with open(fullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                #oneLine = "Antalfai Martin	3,53"
                
                data = oneLine.split("\t")
                # data[0] = "Antalfai Martin"
                # data[1] = "3,53"

                if(data[0] == ''):
                    continue

                student = Student()
                student.name = data[0]
                student.avarage = float(data[1].replace(",", "."))
                #student = { name = "Antalfai Martin", avarage = 3.53 }

                students.append(student)
            
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")

    return students

def wrtiteStudentsToFile(fileName: str, students: List[Student]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding='utf-8', mode="a") as file:
            for student in students:
                file.write(f"{str(student)}")
                
                if(len(students) != index):
                    file.write("\n")
                
                index += 1

        return True
    except FileNotFoundError as ex:
        return False