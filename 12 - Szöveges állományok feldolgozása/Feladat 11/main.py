from nobel import*
from typing import*
from fileService import*
from nobelService import*
import os

os.system("cls")
fileName:str="nobel.csv"

nobels:List[Nobel]=nobelFromFile(fileName)
#3
McType:str=getMcType(nobels)
print (f"{McType}")
#4
names=getLiterary2017(nobels)
print(f"{names}")
#5
#organizationsFrom1990:Dict[int,str]=getOrganizationsFrom1990(nobels)

#yearAndOrganizations=printRecent()
#6
curies:List[Nobel]=getCuries(nobels)
print(f"{curies}")
