import random

num:int = random.randint(0,9)
tri:int = 5
guessed:bool = False
guess:str= ""
data:str=""

while(tri >0 and not guessed):
    while(guess == None and (guess > 9 or guess <0)):
        print("kérem a tippet: ")
        data=input()
        isNumber:bool = data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit()
    tri=-1
    if(isNumber):
        guess=int(data)
    if(num==guess and tri>=0):
        guessed=True
        print("talalt")
    elif(num!=guess and tri>0):
        print(f"Nem talalt meg van {tri} probalkozas")
    elif(num!=guess and tri==0):
        print("Nem tlalt,nincs tobb probalkozas")


            
