print("Adjon meg egy számot:", end="")
number:int = int(input())

print("Adjon meg egy másik számot:", end="")
number2:int = int(input())

print("Adjon meg egy harmadik számot:", end="")
number3:int = int(input())

if(number < number2 and number < number3):
    print(f"1.: {number}")

elif(number2 < number and number2 < number3):
    print(f"1.: {number2}")

elif(number3 < number and number3 < number2):
    print(f"1.: {number3}")