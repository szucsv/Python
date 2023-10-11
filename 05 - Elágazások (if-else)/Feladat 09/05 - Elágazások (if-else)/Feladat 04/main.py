print("Adjon meg egy számot:", end="")
number:int = int(input())

print("Adjon meg egy másik számot:", end="")
number2:int = int(input())

if(number > number2):
    print(f"{number} a nagyobb szám")

elif(number < number2):
    print(f"{number2} a nagyobb szám")
else:
    print(f"{number} és {number2}egyenlő")