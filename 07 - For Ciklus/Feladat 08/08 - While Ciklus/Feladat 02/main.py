import os
import time

number:float = None
data:str=""
while(number==None or(number<0 or number>9)):
    print("kérem a szamot: ")
    data=input()
    isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

    if(isNumber ):
        number = float(data.replace(",","."))
    if( isNumber and (number < 0 or number > 9)):
            print("Nem a megfelelo tartomanyban van")
    
            time.sleep(3)
            os.system("cls")

    elif(not isNumber):
            print("\nNem szamot adott meg!")
            time.sleep(3)
            os.system("cls")
print(f" a beolvasott szam {number}")