money:int=0
coins:int=None
data:str=None
isNumber:bool=False
menu:int=None
change:int=0
selectedDrink:str=None

while(money<330):
    while(coins==None or (coins!=50 and coins!=100 and coins !=200)):
        print("dobja be az ermet 50,100,200")
        data=input()
        isNumber = input.replace("-","").isdigit()

        if(not isNumber):
            print("Nem szamot adott meg")
            continue
        
        coins=int(input)
        if(coins !=50 and coins!=100 and coins!=200):
            print("Nem megfelelo az erme")

    money+=coins
    print(f"Bedobott penzosszeg: {money}")
    coins=None


print("Üdítők: \n 1 Ice tea \n 2 Limonádé \n 3 epres jégkása \n 4 Almale \n 5 szénsavmentes víz \n 0 Elállás a vársálástól")

while(menu==None or menu<0 or menu >10):
    print("kerem valasszon")
    data=input()

    isNumber=input.replace("-","").isdigit

    if(not isNumber):
            print("Nem szamot adott meg")
            continue
    menu=int(input)
    if(menu < 0 or menu > 5):
        print("nem letezo menupont")

if(menu==0):
    print(f"kerem vegye el a penzet {money}")
    exit

match(menu):
    case 1:
        selectedDrink="Ice Tea"
    case 2:
        selectedDrink="limonade"
    case 3:
        selectedDrink="epres jegkasa"
    case 4:
        selectedDrink="almale"
    case 5:
        selectedDrink="szensamnetes viz"

change =money-330

if(change!=0):
    print(f"onnek visszajar {change}")
    print("Kerem vegy el a visszajarot")