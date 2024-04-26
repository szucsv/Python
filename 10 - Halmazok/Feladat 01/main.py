from collectionService import *
from typing import *

collection:List[int] = getCollection()

print("a gyujtemeny elemei:")
printCollectionToConsole(collection)

print("a gyujtemeny elemei forditva:")
printReversedCollectionToConsole(collection)

sum:int = getSumOfCollection(collection)
print(f"az elemek osszege: {sum}")

avarage:float = sum / len(collection)
print(f"\n az elemek atlaga : {avarage:.2f}")

evenElements:list[int] = getEvenOfCollection(collection)

print("a gyujtemeny paros elemei:")
printCollectionToConsole(evenElements)

countofOdd:int = getNumberOfOdd(collection)
print(f"a gyujtemenyben ennyi paratlan elem van: {countofOdd}")

countOf0End:int = get0EndNum(collection)
print(f"ennyi 0-ra vegzodo szam van: {countOf0End}")

biggest:int = getBiggestItem(collection)
print(f" a legnagyobb szam: {biggest}")

min:int = getMinNum(collection)
print(f"a legkisebb szam helye: {min}")

getAnIncresingList(collection)
print(f"a gyujtemeny novekvo sorrendben: {collection}")