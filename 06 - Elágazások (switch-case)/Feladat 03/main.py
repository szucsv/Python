selectDrink:int =None
output:str =None
error:str = None

print("1 - Coca Cola")
print("2 - Pepsi")
print("3 - fanta")
print("4 - Sprite")

print(" Kérem az udito sorszamat: " ,end="")
selectDrink = int (input())
match(selectDrink):
    case 1:
        output= "Coca Cola"
    case 2:
        output= "Pepsi"
    case 3:
        output= "Fanta"
    case 4:
        output= "Sprite"
    case _:
        error = " nem letezo"

if(error == None and selectDrink >= 1 and selectDrink <=4):
    print(f" On {output} valasztott. Egeszsegere!")
elif(error != None):
    print(error)