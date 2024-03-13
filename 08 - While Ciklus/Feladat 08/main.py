import os
import time

age:int = None
ageGroup:str=""
data:str=""
while(age==None):
    print("Adja meg az életkorát: ")
    data=input()
    isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

    if(isNumber):
        age = int(data)
        if( age < 0 or age > 99):
            print("Nem a megfelelo tartomanyban van")
            age = None
    elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")

if(age >=0 and age<=6):
    ageGroup = "gyerek"
elif(age >=7 and age<=18):
    ageGroup = "iskolás"
elif(age >=19 and age<=65):
    ageGroup = "dolgozó"
else:
    ageGroup = "nyugdíjas"

print(f"{ageGroup}")