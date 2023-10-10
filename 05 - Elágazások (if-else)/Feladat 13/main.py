print("Adjon meg egy számot::", end="")
number:int = int(input())

if(number > 0 & number < 9):
    print(f"{number} egyjegyű szám")

elif(number > 10 & number < 99):
    print(f"{number} kétjegyű szám")

elif(number > 100 & number < 999):
    print(f"{number} háromjegyű szám")

