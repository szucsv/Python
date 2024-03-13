import random

num:int = random.randint(0,9)
tryy:int = 5
guessed:bool = False
guess:str=None


while(tryy >0 and not guessed):
    print("kérem a tippet: ")
    guess=input()
    
    if(guess.isdigit()):
        guess=int(guess)
        if(num==guess):
            guessed=True
            print("talalt")
        elif( guess > 9 or guess < 0):
            print("nincs tartomanyban") 
        else:
            tryy-=1
            print(f"Nem talalt meg van {tryy} probalkozas")
            if(tryy==0):
                print(f"A szam {num} volt")
    elif(not guess.isdigit()):
        print("Nem szamot adott meg ")
        
#.replace("-","",1)



            
