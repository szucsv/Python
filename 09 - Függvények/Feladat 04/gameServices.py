from consolServices import getIntNumber
def game(randomNum) -> int:
    Guess:int=0
    num:int=None

    while(num==None or (num != randomNum)):
        num = getIntNumber("kerem a szamot")
        Guess+=1
        if(num > randomNum):
                print("kisebb szam")
        else:
                print("nagyobb szam")
    return Guess 