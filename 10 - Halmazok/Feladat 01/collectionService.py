from typing import *
import random

def getCollection(collectionLenght:int = 10) -> list[int]:
    collection:list[int] = []

    for i in range(0, collectionLenght,1):
        collection.append(random.randint(10,99))

    return collection

def printCollectionToConsole(collection:list[int]) -> None:
    for item in collection:
        print(f"{item} \t", end="")

def printReversedCollectionToConsole(collection:list[int]) -> None:
    for index in range(len(collection) -1 ,-1,-1):
        print(f"{collection[index]} \t", end="")

def getSumOfCollection(collection:list[int]) -> int:
    sum:int = 0
    
    for item in collection:
        sum += item
    
    return sum

def getEvenOfCollection(collection:list[int]) -> list[int]:
    evenElements:list[int] = []

    for item in collection:
        if(item % 2 == 0):
            evenElements.append(item)
    
    return evenElements

def getNumberOfOdd(collection:list[int]) -> int:
    count:int = 0
    for item in collection:
        if(item %2 == 1):
            count += 1

    return count

def get0EndNum(collection:list[int]) -> int:
    count:int = 0
    for item in collection:
        if(item %10 == 0):
            count += 1

    return count

def getBiggestItem(collection:list[int]) -> int:
    base:int = collection[0]
    for index in range(1,len(collection),1):
        if(collection[index] > base):
            base = collection[index]

        
    return base

def getMinNum(collection:list[int]) -> int:
    index:int = 0
    min :int = collection[0]
    for i in range(1,len(collection),1):
        if(collection[i] < min):
            min = collection[i]
            index = i
    
    return index

def getAnIncresingList(collection:list[int]) -> None:
    temp:int = None
    for i in range(0, len(collection)-1,1):
        for j in range(i + 1, len(collection),1):
            if(collection[j] < collection[i]):
                temp = collection[i]
                collection[i] = collection[j]
                collection[j] = temp
    
