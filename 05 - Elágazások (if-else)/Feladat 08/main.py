print("Adjon meg egy számot:", end="")
number:int = int(input())

if(number %4 == 0 and number %6 == 0):
    print(f"A szám osztható 4-el és 6-al")
else:
    print(f"A szám nem osztható 4-el és 6-tal")