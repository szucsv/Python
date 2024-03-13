import os
import time 

max:int=None
newNumber:int=None
data:str=""
while(newNumber == None or newNumber != 0):
    print("adja meg az elso egesz szamot:", end="")
    data = input()
    
    isNumber: bool = data.replace("-", "", 1).isdigit()

    if(isNumber):
        newNumber=int(data)

    elif(not isNumber):
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")

    if(max==None):
        max=newNumber
    elif(newNumber>=max):
        max = newNumber
 
print(f"legnagyobb szám: {max}")

    