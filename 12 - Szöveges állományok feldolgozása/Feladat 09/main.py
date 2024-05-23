from typing import List

from freight import Freight
from driverIncome import DriverIncome
from fileService import *
from freightService import *

freights:List[Freight] = getFreightsFromFile("fuvar.csv")
      
#3
print(f"3. feladat: {len(freights)} fuvar")

#4
driverIncome:DriverIncome = getDriverIncomeForDriver(freights, 6185)
print(f"\n4. frladat: {driverIncome.numberOfrides} fuvar alatt ${driverIncome.income}")

#5
paymentTypeCounts: Dict[str, int] = getPaymentTypeCounts(freights)
printPaymentTypesCountOnConsole(paymentTypeCounts)

#6
distanceSumInMiles: float = getSumOfDistanceInKM(freights)
print(f"\n6. feladat: {distanceSumInMiles:.2f} fuvar")

#7
orderFreightsByTravelingTimeDescending(freights)
longestFreight:Freight = freights[0]
print("\n7. feladat: A leghosszabb fuvar:")
print(f"Fuvar hossza: {longestFreight.travelTime}")
print(f"Taxi azonosito: {longestFreight.id}")
print(f"Megtett tavolsag: {longestFreight.distance}")
print(f"Viteldij: ${longestFreight.fare:.2f}")

#8
freightErrors:List[Freight] = getFreightErrors(freights)
erroFileCreated: bool = saveFreightsWithError("hibak.txt", freightErrors)
if(erroFileCreated):
    print(f"8. feldat: hibak.txt letrehozva")
else:
    print(f"8. feldat: hibak.txt nem lett letrehozva")
    