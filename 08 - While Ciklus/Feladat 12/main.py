import os
import time 

interest:int=None
month:int=0
while(interest == None or interest > 100000 ):
    print("adja meg a megktakaritott penzet:", end="")
    data = input()
    
    isStart: bool = data.replace("-", "", 1).isdigit()

    if(isStart):
        interest = int(data) 
        if(interest > 100000 ):
            print("\nNagyobb az elérni kívánt célnél")
            time.sleep(3)
            os.system("cls")
    elif(not isStart):
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")
while(interest < 100000):
    interest+=interest*0.02
    month+=1
    
print(f"{month} honap alatt eri el a 100000et ")    


