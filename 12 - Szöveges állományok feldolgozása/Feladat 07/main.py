from typing import List

from euStateJoinDate import EuStateJoinDate
from fileService import *
from statesJoinDateService import *

#2
euStateJoinDates:List[EuStateJoinDate] = getEuStatesWithJoinDateFromFile("EUcsatlakozas.txt")

#3
numberOfEuStatesIn2018: int = getMumberOfStatesBefore(euStateJoinDates, 2018)
print(f"#3: EU tagallamainak szama: {numberOfEuStatesIn2018} db")

#4
numberOfStatesJoinedAt2007: int = getMumberOfStatesJoinedAt(euStateJoinDates, 2007)
print(f"#4: 2007-ben {numberOfStatesJoinedAt2007} orszag csatlakozott")

#5
joinedDateOfHungary = getJoinedDateOfState(euStateJoinDates, "Magyarorsz�g")
print(f"#5: Magyarorszag csatlakozasanak datuma: {joinedDateOfHungary.year}.{joinedDateOfHungary.month}.{joinedDateOfHungary.day}")

#6
wasAnyJoiningInMonth: bool = wasAnyJoiningInMonth(euStateJoinDates, 5)
if(wasAnyJoiningInMonth):
    print("#6: Majusban volt csatlakozas")
else:
    print("#6: Majusban nem volt csatlakozas")

#7
orderEuStatesByJoinDatesDescending(euStateJoinDates)
lastJOinedEuState: EuStateJoinDate = euStateJoinDates[0]
print(f"#7: Legutoljara csatlakozott orszag: {lastJOinedEuState.state}")

#8
numberStatesByJoiningYears: Dict[int, int] = groupNumberStatesByJoiningYears(euStateJoinDates)
print("#8: Statisztika")
printNumberOfStatesGroupedByJoiningYear(numberStatesByJoiningYears)
    