import random

num:int = random.randint(0,9)
tryy:int = 5
guessed:bool = False
guess:str=None


while(tryy >0 and not guessed):
    while(number==None or(number<0 or number>9)):
        print("kérem a szamot: ")
        data=input()
        isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()

        if(isNumber ):
            number = int()(data)
        if( number < 0 or number > 9):
            print("Nem a megfelelo tartomanyban van")


        elif(not isNumber):
                print("\nNem szamot adott meg!")
                
                
                tryy-=1
    if(number == num):
        guessed = True
    else:
        print(f"nem talalta el, probalkozasok szam: {tryy}")
        number = None
if (guessed):
    print(f"eltalalta")
else:
    print(f"")
               

print(f" a beolvasott szam {number}")