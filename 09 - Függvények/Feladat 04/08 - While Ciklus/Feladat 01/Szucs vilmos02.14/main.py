import time
import os

data:str=""
data2:str=""
money:int=0
coin:int=None
drinknum:int=None
drink:str=""
change:int=0
while(money==None or money < 330):
    print("Kerem a penzt(50-es,100-as,200-as) :")
    data= input()

    isNumber:bool=data.isdigit()

    if(isNumber):
        coin=int(data)
        if(coin==50):
            money+=50
            print(f"eddig {money} forintot dobott be")
        elif(coin==100):
            money+=100
            print(f"eddig {money} forintot dobott be")
        elif(coin==200):
            money+=200
            print(f"eddig {money} forintot dobott be")
    elif(not isNumber):
        print("nem szamot adott meg")
        time.sleep(3)
        os.system("cls")

print("Üdítők: \n 1 Ice tea \n 2 Limonádé \n 3 epres jégkása \n 4 Almale \n 5 szénsavmentes víz \n 0 Elállás a vársálástól")
while(drink==""):
    print("Kerem az udito szamat: ")
    data=input()
    isNumber:bool=data.isdigit()
    if(isNumber):
        drink=int(data)
    elif(not isNumber):
        print("Nem szamot adott meg")
        time.sleep(3)
        os.system("cls")
change=money-330
match(drink):
    case 0:
        print(f"Visszalépett , itt a pénze :{money}")
        money=0
        change=0
    case 1:
        drink="ice tea"
    case 2:
        drink="limonade"
    case 3:
        drink="epres jegkasa"
    case 4:
        drink="almale"
    case 5:
        drink="szensavmentes viz"
    case _:
        print("Olyan szamot adott meg,ami nem udito sorszam")
if(drink=="ice tea" or drink=="limonade" or drink=="epres jegkasa" or drink=="almale" or drink=="szensavmentes viz"):
    print(f" Ön {drink}-et választott. Egészségere!")        
    print(f"Önnek visszajár {change} Ft! \n Kérem, vegye el a visszajárót az automatából.")
        