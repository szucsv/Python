print("Adjon meg egy számot:", end="")
number:int = int(input())

if(number %5 == 0):
    print(f" A szám osztahó öttel")
else:
    print(f"A szám nem osztható öttel")