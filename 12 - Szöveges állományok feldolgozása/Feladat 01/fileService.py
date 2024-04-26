from typing import *
from io import open
import os
from student import Student

fileName:str="adatok.txt"

def getFileFullPath(fileName:str )-> str:

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fullpath: str = os.path.join(basepath,fileName)

    return fullpath

def getStudentFromFile(fileName:str)->List[Student]:
    students:List[Student]=[]
    student:Student=None
    oneList:str=None

    try:
        here: str = os.path.dirname(os.path.abspath(__file__))
        path: str = os.path.join(here,fileName)

        with open(path, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()

                data=oneLine.split("\t")
                #data[0]="Antalfalvi Martin"
                #data[1]="3,53"

                if(len(data[0])==""):
                    continue

                student=Student()
                student.name=data[0]
                student.avarage=float(data[1].replace(",","."))

                students.append(student)

    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato!")

    return students

def  writeStudentsToFile(filename:str,students:List[Student])->bool:
     try:
        fullpath:str=getFileFullPath(filename)

        with open (fullpath,encoding='utf-8',mode="a") as file:
            for (student,index) in students:
                file.write(f"{str(student)}")
                if(len(students)-1 !=index):
                    file.write("\n")

                    index+=1


        return True
     except FileNotFoundError as ex:
        return False