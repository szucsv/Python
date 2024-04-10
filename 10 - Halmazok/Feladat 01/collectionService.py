from typing import*
import random

def getCollection(collectionLength:int=10) -> list[int]:
    collection:List[int]=[]

    for i in range(0,collectionLength,1):
        collection.append(random.randint(10,99))


    return collection
def printCollectionToConsole(collection:List[int])->None:
    for item in collection:
        print(f"{item}\t",end="")

def printReversedCollectiontoConsole(collection:List[int])->None:
    for index in range(len(collection)-1,-1,-1):
        print(f"{collection[index]}\t",end="")

def getSumOfCollection(collection:List[int])->int:
    sum:int=0

    for item in collection:
        sum+=item

    return sum

def getEvenElementsOfCollection(collection:List[int])->list[int]:
    evenElements:List[int]=[]

    for item in collection:
        if(item%2==0):
            evenElements.append(item)
    
    return evenElements