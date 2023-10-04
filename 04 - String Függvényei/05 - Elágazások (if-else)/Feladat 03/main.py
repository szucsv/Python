print("Adjon meg egy számot:", end="")
number:int = int(input())

if(number > -30 and number < 40):
    print(f"{number} -30 és 40 között van")
else:
    print(f"{number} nincs -30 és 40 között")