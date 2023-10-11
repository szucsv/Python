print("Adjon meg egy számot::", end="")
number:int = int(input())

if(number %2 == 0):
    print("A szám páros")
else:
    print("A szám nem páros") 

if(number> 0):
    print("A szám pozitív")
elif(number < 0):
    print("A szám negatív")
else:
    print("A szám nulla")


if(number % 5 == 0):
    print("A szám osztható öttel")
else:
    print("A szám nem osztható öttel")
