from student import Student
from fileService import getStutentsFromFile, wrtiteStudentsToFile
from studentService import *
from typing import *

students: List[Student] = getStutentsFromFile("adatok.txt")

#1 - Írjuk ki minden diák adatát a képernyőre!
printStudentsToConsole(students)

#2 - Hány diák jár az osztályba?
print(f"\nAz osztalynak: {len(students)} tanulojja van.")

#3 - Mennyi az osztály átlaga?
avarage: float = getStudentsAvarage(students)
print(f"\nAz osztaly atgala: {avarage:.2f}")

#4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
#   NEM BIZTOS, HOGY CSAK 1 VAN !!!
bestStudents: List[Student] = getBestStudents(students)
print(f"\nAz osztaly legjobb tanuloi:")
printStudentsToConsole(bestStudents)

#5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
studentsAboveAvarage: List[Student] = getStudentsAboveAvarage(students, avarage)
isFileWriteSuccess: bool = wrtiteStudentsToFile("atlagfelett.txt", studentsAboveAvarage)
if(isFileWriteSuccess):
    print("\natlagfelett.txt allomány mentese sikeres volt")
else:
    print("\natlagfelett.txt allomány mentese nem volt sikeres")

#6 - Van e kitünő tanulónk?
isAnyExcelentStudent: bool = isAnyExcellentStudent(students)
if(isAnyExcelentStudent):
    print("\nVan kituno tanulo")
else:
    print("\nNincs kituno tanulo")

"""
7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
    Értékhatárok:
	- elégtelen, ha: 0.00 - 1.99
	- elégséges, ha: 2.00 - 2.99
	- jó, ha: 3.00 - 3.99
	- jeles, ha: 4.00 - 4.99
	- kitünő, ha: 5.00
"""
print("\nA diakok ertekhatarai:")
studentCategories: Dict[str, int] = getStudentCategoriesCount(students)
printStudentCategoriesToConsole(studentCategories)