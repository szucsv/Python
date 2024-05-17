import datetime
from typing import Dict, List, Set

from euStateJoinDate import EuStateJoinDate

def getMumberOfStatesBefore(euStateJoinDates:List[EuStateJoinDate], joinedTillYear: int) ->int:
    counter: int = 0

    for euStateJoinDate in euStateJoinDates:
        if(euStateJoinDate.joinDate.year <= joinedTillYear):
            counter += 1

    return counter

def getMumberOfStatesJoinedAt(euStateJoinDates:List[EuStateJoinDate], joinedYear: int) ->int:
    counter: int = 0

    for euStateJoinDate in euStateJoinDates:
        if(euStateJoinDate.joinDate.year == joinedYear):
            counter += 1

    return counter

def getJoinedDateOfState(euStateJoinDates:List[EuStateJoinDate], state: str) -> datetime.date:
    joinedDate: datetime.date = None

    for euStateJoinDate in euStateJoinDates:
        if(euStateJoinDate.state.lower() == state.lower()):
            joinedDate = euStateJoinDate.joinDate
            break

    return joinedDate

def wasAnyJoiningInMonth(euStateJoinDates:List[EuStateJoinDate], month: int) -> bool:
    for euStateJoinDate in euStateJoinDates:
        if(euStateJoinDate.joinDate.month == month):
            return True
        
    return False

def orderEuStatesByJoinDatesDescending(euStateJoinDates:List[EuStateJoinDate]) -> None:
    temp: euStateJoinDates = None
    
    for i in range (0, len(euStateJoinDates), 1):
        for j in range(i + 1, len(euStateJoinDates), 1):
            if(euStateJoinDates[j].joinDate > euStateJoinDates[i].joinDate):
                temp = euStateJoinDates[i]
                euStateJoinDates[i] = euStateJoinDates[j]
                euStateJoinDates[j] = temp

def getJoiningYears(euStateJoinDates:List[EuStateJoinDate]) -> Set[int]:
    joiningYears: Set[int] = set()
    
    for euStateJoinDate in euStateJoinDates:
        joiningYears.add(euStateJoinDate.joinDate.year)

    return joiningYears

def groupNumberStatesByJoiningYears(euStateJoinDates:List[EuStateJoinDate]) -> Dict[int, int]:
    numberStatesByJoiningYears: Dict[int, int] = {}

    joiningYears: Set[int] = getJoiningYears(euStateJoinDates)
    for joiningYear in joiningYears:
        numberStatesByJoiningYears[joiningYear] = 0

    for joiningYear in joiningYears:
        counter: int = getMumberOfStatesJoinedAt(joiningYear)
        numberStatesByJoiningYears[joiningYear] = counter

    # for euStateJoinDate in euStateJoinDates:
    #    numberStatesByJoiningYears[euStateJoinDate.joinDate.year] += 1

    return numberStatesByJoiningYears

def printNumberOfStatesGroupedByJoiningYear(numberOfStatesByJoiningYears: Dict[int, int]) -> None:
    for year, numberOfJoinedState in numberOfStatesByJoiningYears.items():
        print(f"\t{year} - {numberOfJoinedState} orszag")