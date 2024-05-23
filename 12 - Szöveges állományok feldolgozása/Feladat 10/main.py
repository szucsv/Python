<<<<<<< HEAD
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
=======
import random
from typing import List

from pilot import Pilot
from fileService import *
from pilotService import *

#2
pilots:List[Pilot] = getPilotsFromFile("pilotak.csv")

#3
print(f"\n3. feldat: {len(pilots)}")

#4
lastIndex: int = len(pilots) - 1
lastPilotInCollection: Pilot = pilots[lastIndex]
print(f"\n4. feladat: {lastPilotInCollection.name}")

#5
pilotsBornBeforeCentury: List[Pilot] = getPilotsBornBeforeCentury(pilots, 19)
print("\n5. feladat:")
printPilotsBornBeforeCentury(pilotsBornBeforeCentury)

#6
pilotWithTheLowerStartingNumber: Pilot  = getPilotWithTheLowerStartingNumber(pilots)
print(f"\n6. feldat: {pilotWithTheLowerStartingNumber.nationality}")

#7
notUniqueStartNumbers: List[int] = getMultiplyTimesUsedStartingNumber(pilots)
print(f"\n7. feldat: {notUniqueStartNumbers}")
>>>>>>> 012d0f9b88d5e22b861ced892eb512ee28d60415
