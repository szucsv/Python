import os
import time

data: str = ""
number : int = None
divByTwo: str = ""
sumWFive: int = 0
divByEleven: int = 0
divWRemainder: str = ""

while((number == None) or(number <0 or number > 99)):
    print("adjon meg egy max 2 jegyu pozitiv szamot:", end="")
    data = input()
    
    isNumber: bool = data.replace("-", "", 1).isdigit()

    if(isNumber):
        number = int(data) 
        if(number < 0 or number > 99):
            print("\ntul nagy vagy negaiv")
            time.sleep(3)
            os.system("cls")
    elif(not isNumber):
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

for i in range(0, number+1, 1):
    if(i % 2 == 0):
        divByTwo += f"{i},"
    if(i % 5 == 0):
        sumWFive += i
    if(i % 11 == 0):  
        divByEleven += 1
    if(i % 7 == 3):
        divWRemainder += f"{i},"

print(f"Paros szamok:{divByTwo}\n 0 és {number} közt az 5-tel oszthato szamok osszege:{sumWFive}\n 11-el oszthato szamok szama: {divByEleven}\n 7-tel osztas utan 3 maradekul: {divWRemainder}")