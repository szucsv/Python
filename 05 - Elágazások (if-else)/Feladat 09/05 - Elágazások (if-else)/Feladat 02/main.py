print("Adjon meg egy számot:" , end="")
number:int = int(input())

if(number >= 0):
    print(f"{number} pozitív")

else:
    print(f"{number} negatív")