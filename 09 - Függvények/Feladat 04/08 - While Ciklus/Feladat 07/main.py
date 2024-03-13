import time
import os

smaller:int = None
bigger:int = None

while(smaller == None):
        print("Kerem a szamot:")
        data = input()

        issmaller:int = data.replace("-","").isdigit()

        if(issmaller):
            smaller = int(data)

        elif(not issmaller):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")

while(bigger == None):
        print("Kerem a szamot,ami nagyobb az elsőnél")
        data = input()
        issmaller:int = data.replace("-","").isdigit()

        if(issmaller):
            bigger = int(data)
            if(bigger <= smaller):
                 bigger = None
                 print("Kisebb vagy egyenlo szamot adott meg")
                 time.sleep(3)
                 os.system("cls")

        elif(not issmaller):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")

for i in range(bigger,smaller-1,-1):
    print(i)
