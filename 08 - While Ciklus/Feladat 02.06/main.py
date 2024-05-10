import os
import time

data:str=""
number:int=None
while(number==None or(number<-99 or number>99)):
    print("kérem a max ketjegyu szamot: ")
    data=input()
    isNumber:bool = data.replace("-","",1).isdigit()

    if(isNumber ):
        number = data
    if( isNumber and (number< -99 or number>99)):
            print("Nem a megfelelo tartomanyban van")
    
            time.sleep(3)
            os.system("cls")

    elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")