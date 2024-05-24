from typing import *

from fileService import *
from physicistService import *
from physicist import Physicist

#2
physicists:List[Physicist] = getPilotsFromFile("nobel.csv")


#3
subject: str = getPrizeTypeForPhysicistByName(physicists, "Arthur B. McDonald")
if(subject != None):
    print(f"\n3. feldat: {subject}")
else:
    print(f"\n3. feldat: Ilyen nevvel tudos nem kapott Nobel dijjat")

#4
winnersNameForYear: str = getWinnerNameForYear(physicists, 2017, "irodalmi")
print(f"\n4. feldat: {winnersNameForYear}")

#5
winningOrganisations:List[Physicist] = getWinningOrganisationsFromYear(physicists, 1990, "béke")
print(f"\n5. feldat:")
printPhysicistOnConsole(winningOrganisations)

#6
curieFamilyWons:List[Physicist] = getCurieFamilyWons(physicists)
print(f"\n6. feldat:")
printPhysicistOnConsole(curieFamilyWons)

#7
prizeCountByTypes: Dict[str, int] = getPrizeCountByTypes(physicists)
print(f"\n7. feldat:")
printPrizeCountByTypes(prizeCountByTypes)

#8
prizeTypeWons:List[Physicist] = getWonsForPrizeType(physicists, "orvosi")
isSaved: bool = savePhysicists("orvosi.txt", prizeTypeWons)
if(isSaved):
    print(f"\n8. feldat: mentes sikeres volt")
else:
    print(f"\n8. feldat: mentes sikertelen")
    