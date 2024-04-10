from typing import *
from collectionService import *


collection:list[str] = getCollection()

print("A gyujtemeny elemei:")
printCollectionToConsole(collection)

print("A gyujtemeny elemei forditott sorrendben")
printReversedCollectiontoConsole(collection)

sum:int=getSumOfCollection(collection)
print(f"Az elemek osszege: {sum}")

avarage:float= sum/len(collection)
print(f"\nAz elemek átlaga: {avarage:.2f}")

evenElements:List[int]=getEvenElementsOfCollection(collection)
print("\nA gyujtemeny paros elemei:")
printCollectionToConsole(evenElements)