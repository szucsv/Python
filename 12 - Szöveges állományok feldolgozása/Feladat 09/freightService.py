from typing import Dict, List, Set

from driverIncome import DriverIncome
from freight import Freight


def getDriverIncomeForDriver(freights:List[Freight], driverId: int) -> DriverIncome:
    driverIncome:DriverIncome = DriverIncome()

    for freight in freights:
        if(freight.id == driverId):
            driverIncome.income += (freight.fare + freight.tip)
            driverIncome.numberOfrides += 1

    return driverIncome

def getPaymentTypes(freights:List[Freight]) -> Set[str]:
    paymentTypes: Set[str] = set()

    for freight in freights:
        paymentTypes.add(freight.paymentType)

    return paymentTypes

def getPaymentTypeCounts(freights:List[Freight]) -> Dict[str, int]:
    paymentTypeCounts: Dict[str, int] = {}
    paymentTypes: Set[str] = getPaymentTypes(freights)

    for paymentType in paymentTypes:
        paymentTypeCounts[paymentType] = 0

    for freight in freights:
        paymentTypeCounts[freight.paymentType] += 1

    return paymentTypeCounts

def printPaymentTypesCountOnConsole(paymentTypes:Dict[str, int]) -> None:
    print("\n5. feladat:")

    for paymentType, numberOfPaymentType in paymentTypes.items():
        print(f"\t{paymentType}: {numberOfPaymentType} fuvar")

def getSumOfDistanceInKM(freights:List[Freight]) -> float:
    distanceSumInMiles: float = 0

    for freight in freights:
        distanceSumInMiles += freight.distance

    return distanceSumInMiles * 1.6

def orderFreightsByTravelingTimeDescending(freights:List[Freight]) -> None:
    temp: Freight = None

    for i in range(0, len(freights) - 1, 1):
        for j in range(i+1, len(freights), 1):
            if(freights[j].travelTime > freights[i].travelTime):
                temp = freights[i]
                freights[i] = freights[j]
                freights[j] = temp

def getLongestFreights(freights:List[Freight]) -> Freight:
    longestFreight: Freight = freights[0]

    for index in range(1, len(freights), 1):
        if(freights[index].travelTime > longestFreight.travelTime):
            longestFreight = freights[index]

    return longestFreight

def getFreightErrors(freights:List[Freight]) -> List[Freight]:
    freightErrors:List[Freight] = []

    for freight in freights:
        if(freight.fare > 0 and freight.travelTime > 0 and freight.distance == 0):
            freightErrors.append(freight)

    return freightErrors