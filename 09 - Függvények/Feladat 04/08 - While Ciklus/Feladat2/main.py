import os  
import time

name :  str = None
data : str = ""

while(name== None):
    print("Kérem a nevét: ",end="")
    data=input()

    isName :bool = data.isalpha()
    if(isName):
        name = str(data)
    if (isName and len(name) <= 1):
        print("Nem nevet adott meg")
        time.sleep(3)
        os.system("cls")
    elif(not isName):
        print("Szam van benne")
        time.sleep(3)
        os.system("cls")

print(f"Hello {name} !")