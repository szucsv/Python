sum:int=0
counter:int=0
number:int=None
while(sum<100):
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
    print(f"osszeadasainak szama:{counter}")
