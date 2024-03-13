import os
import time
number:int=None
data:str=""

while(number==None or (number>=-99 and number<100) and number<-999 or number>999 ):
    print(f"Kérem a háromjegyű számot")
    data=input()
    isnumber:bool =data.replace("-","").isdigit()


    if(isnumber):
        number = int(data)
        if((number>=-99 and number<100) and number<-999 or number>999 ):
            print("Nem a megfelelo tartomanyban van")
    elif(not isnumber):
            print("\nNem szamot adott meg!")
if(number % 7 == 0):
    print("A szám oszthato hettel")
else:
    print("A szám nem oszthato hettel")
