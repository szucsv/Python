print("Adjon meg egy számot:", end="")
number:int = int(input())

print("Adjon meg egy másik számot:", end="")
number2:int = int(input())

if(number > number2):
    print(f"1. :{number2} 2. :{number}")
elif(number < number2):
    print(f"1.: {number} \n 2.: {number2}")
else:
    print(f"A két szám egyenlő")