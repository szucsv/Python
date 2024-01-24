import random

num:int = random.randint(0,9)
tri:int = 5
guessed:bool = False
guess:str=None


while(tri >0 and not guessed):
    print("kérem a tippet: ")
    guess=input()
    
    if(guess.isdigit()):
        guess=int(guess)

        if(num==guess):
            guessed=True
            print("talalt")
        else:
            tri-=1
            print(f"Nem talalt meg van {tri} probalkozas")
            if(tri==0):
                print(f"A szam {num} volt")
    elif (not guess.isdigit()):
        print("Nem szamot adott meg")   




            
