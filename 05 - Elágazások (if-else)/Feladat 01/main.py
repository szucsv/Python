
print("Adjon meg egy számot:", end="")
number:int = int(input())

if(number > 0):
    print(f"{number} nagyobb 0-nal")

elif(number < 0):
    print(f"{number} kisebb 0-nal")

else:
    print(f"A beírt szám 0")
    