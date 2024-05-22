from typing import *
from pilots import *
from fileService import *
from pilotService import *
filename:str="pilotak.csv"

pilots:List[Pilot]=getPilotsFromFile(filename)
#3
print(len(pilots))
#4
print(pilots[-1].name)
#5
yearAndPilot:Dict[str,str]=yearAndPilot(pilots)
printRecent()
#6
