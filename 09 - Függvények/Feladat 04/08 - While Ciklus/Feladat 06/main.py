number:int=None
counter:int=0
sum:int=0
bord:int=0

while(bord==0):
    print("kérem a szaznal nagyobb szamot: ")
    data=input()
    isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

    if(isNumber ):
        number = int(data.replace(",","."))
    if( isNumber and (number<100)):
        print("Nem a megfelelo tartomanyban van")

    elif(not isNumber):
        print("\nNem szamot adott meg!")
    bord+=number

while(sum<bord):
    while(number==None):
        print("kérem a szamot: ")
        data=input()
        isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

        if(isNumber ):
            number = int(data.replace(",","."))
        elif(not isNumber):
            print("\nNem szamot adott meg!")
        sum+=number
    number=None
    counter+=1
   
    print(f"ez az osszege:{sum}")
print(f"ennyi lepesben erte el a hatarerteket:{counter}")



