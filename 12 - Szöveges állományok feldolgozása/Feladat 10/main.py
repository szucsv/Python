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