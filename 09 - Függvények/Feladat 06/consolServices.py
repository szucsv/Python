import os
import time

def getIntNumber() -> int:

    number:int=None


    number:float = None
    data:str=""
    while(number==None ):
        print("kérem a szamot: ")
        data=input()
        isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

        if(isNumber ):
            number = float(data.replace(",","."))


        elif(not isNumber):
                print("\nNem szamot adott meg!")
                time.sleep(3)
                os.system("cls")
    return number 

def getName(prompt:str) -> str:
    name=None
    data:str=""

    while (name == None or len(name) <2 or not name.isalpha()):
        print("Adja meg a nevet: ")
        name = input()

        areAllLettersInString = name.isalpha
    
    if(areAllLettersInString and len(name)<2):
        print("lealabb 2 karakternek kell lennie")

    if(not areAllLettersInString):
        print("A nevben csak betuk lehetnek")
    os.system("cls")
    return name

def maxButNoMin(prompt:str, max:int) -> int:

    number:int = None
    data:str
    
    while(number == None or number > max):
        print(f"{prompt} [{max}]",end=": ")
        data = input()
        isNumber: bool = data.replace("-", "",1).isdigit()
        if(isNumber):
            number = int(data)
            if(number > max):
                print("\nNincs tartományban!")
                time.sleep(2)
                os.system("cls")
        else:
            print("\nSzámot adjon meg!")
            time.sleep(2)
            os.system("cls")
    return number

def minButNoMax(prompt:str, min:int) -> int:

    number:int = None
    data:str
    
    while(number == None or number < min):
        print(f"{prompt} [{min}]",end=": ")
        data = input()
        isNumber: bool = data.replace("-", "",1).isdigit()
        if(isNumber):
            number = int(data)
            if(number < min):
                print("\nNincs tartományban!")
                time.sleep(2)
                os.system("cls")
        else:
            print("\nSzámot adjon meg!")
            time.sleep(2)
            os.system("cls")
    return number

def inBetween(min:int, max:int, prompt:str = "Kérem adjon meg egy a két szám közti számot") -> int:

    number:int = None
    data:str
    
    while(number == None or (number < min or number > max)):
        print(f"{prompt} [{min}, {max}]",end=": ")
        data = input()
        isNumber: bool = data.replace("-", "",1).isdigit()
        if(isNumber):
            number = int(data)
            if(number < min or number > max):
                print("\nNincs tartományban!")
                time.sleep(2)
                os.system("cls")
        else:
            print("\nSzámot adjon meg!")
            time.sleep(2)
            os.system("cls")

    return number

def oneLetter(prompt:str = "Kérem adjon meg egy betűt") -> str:
    data:str = None
    isletter:bool = False

    while(data == None or not isletter):
        print(f"{prompt}", end=": ")
        data = input()

        isletter = len(data) == 1 and data.isalpha()

        if(not isletter):
            print("\nKérem csak egy betűt adjon meg!")
            time.sleep(2)
            os.system("cls")


    return data

def oneSpecificLetter(prompt:str, goodLetters:list[str]) -> str:
    data:str = None
    isletter:bool = False

    while(data == None or not isletter):
        print(f"{prompt} {goodLetters}", end=": ")
        data = input()

        isletter = len(data) == 1 and data.isalpha() and (data in goodLetters)

        if(not isletter):
            print("\nKérem csak egy megfelelő betűt adjon meg!")
            time.sleep(2)
            os.system("cls")
