from student import Student
from fileService import *
from typing import *
from studentService import *

students:List[Student]=getStudentFromFile("adatok.txt")

printStudentsToConsole(students)

print(f"Az osztálynak :{len(students)} tanuloja van.")

avarage:float= getStudentsAvarage(students)
print(f"\n Az osztaly atlaga{avarage:.2f}:")

#BestStudents:List[Student] = getBestStudents(students)
#print(f"a legtobb atlagu diak neve es atlaga:")
#printStudentsToConsole(BestStudents)

#getStudentsAboveAvarage:List[Student]=getStudentsAboveAvarage(students,avarage)
#isFileWriteSucces:bool=writeStudentsToFile("atlagfelett.txt")
#if(isFileWriteSucces):
#    print(f"az atlagfeletti allomany mentese sikeres volt")
#else:
#        print(f"az atlagfeletti allomany mentese sikertelen volt")

isAnyExcellent:bool=isAnyExcellentStudent(students)
if(isAnyExcellent):
      print("van kituno")
else:
      print("nincs")
grades: Dict[str, int] = getGradesFromStrudents(students)

#print(f"{grades}")
print("\nA diákok értékhatárai")
studentCategories:Dict[str,int]=getStudentCategoriesCount(students)
printStudentCategoriesToConsole(studentCategories)