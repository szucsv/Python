
serial:int = None
drink:str = ""

print("Válasszon egy üdítőt: \n 1: Coca-Cola \n 2: Fanta \n 3: Sprite \n 4: Kőbányai \n 5: SIÓ Almaüdítőital")

while(serial == None ):
    print("Adja meg az üdítő sorszámát ")
    data=input()
    isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

    if(isNumber):
        serial = int(data)
        if(serial < 0 or serial > 5):
            print("Nem a megfelelo tartomanyban van")
            serial=None
    elif(not isNumber):
            print("\nNem szamot adott meg!")
match(serial):
    case 1:
        drink="Coca-Cola"
    case 2:
        drink="Fanta"
    case 3:
        drink="Sprite"
    case 4:
        drink="Kőbányai"
    case 5:
        drink="SIÓ Almaüdítőital"

print(f"Ön választasa: {drink}")
