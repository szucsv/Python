import time
import os

num:int = None
biggerNumber:int = None

while(num == None):
        print("Kerem a szamot:")
        data = input()

        isNumber:int = data.isdigit()

        if(isNumber):
            num = int(data)

        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")
while(biggerNumber == None):
        print("Kerem a szamot,ami nagyobb az elsőnél")
        data = input()

        isNumber:int = data.isdigit()

        if(isNumber):
            biggerNumber = int(data)
            if(biggerNumber < num):
                 biggerNumber = None
                 print("Kisebb szamot adott meg")
                 time.sleep(3)
                 os.system("cls")

        elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")
for i in range(biggerNumber,num,-1):
    print(i)
