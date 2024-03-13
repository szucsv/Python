def game(randomNum) -> int:
    Guess:int=0
    num:int=None

    while(num==None or (num != randomNum)):
            print("kérem a szamot: ")
            data=input()
            isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

            if(isNumber ):
                num = float(data.replace(",","."))


            elif(not isNumber):
                print("\nNem szamot adott meg!")

            Guess+=1
            if(isNumber and num > randomNum):
                print("kisebb szam")
            else:
                print("nagyobb szam")
    return Guess 