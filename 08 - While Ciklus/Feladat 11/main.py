import os
import time 
import random

smaller:int=None
bigger:int=None
avarage:float=None
div:int = 0
while(smaller == None or smaller % 2  != 0):
    print("adjon meg egy paros kisebb szamot:", end="")
    data = input()
    
    isSmaller: bool = data.replace("-", "", 1).isdigit()

    if(isSmaller):
        smaller = int(data) 
        if(smaller % 2  != 0):
            print("\nNem paros")
            time.sleep(3)
            os.system("cls")
    elif(not isSmaller):
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

while(bigger == None or bigger % 2  == 0 or bigger<smaller):
    print("adjon meg egy paratlan nagyobb szamot:", end="")
    data = input()
    
    isBigger: bool = data.replace("-", "", 1).isdigit()

    if(isBigger):
        bigger = int(data) 
        if(bigger % 2  == 0):
            print("\nNem paratlan")
            time.sleep(3)
            os.system("cls")
        elif(bigger<=smaller):
            print("A szam nem nagyobb az elozonel")
    elif(not isBigger):
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

randomnum:int = random.randint(smaller,bigger)

if(randomnum-smaller<bigger-randomnum):
    print("a kisebb szamhoz van kozelebb")
else:
    print("a nagyobb szamhoz van kozelebb")

avarage=(smaller+bigger)/2

print(f"Az atlaga: {avarage}")

for i in range(smaller,bigger,1):
    if i % 4 == 0:
        div+=1

print(f"Neggyel oszthato szamok:{div}")