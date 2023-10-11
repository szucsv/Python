print("Adjon meg egy számot:", end="")
number:int = int(input())

if(number > 10 and number < 20):
    print(f"{number} 10 és 20 között van")
elif(number < -10 and number > -20):
    print(f"{number} -10 és -20 között van")
else:
    print(f"{number} nincs 10 és 20 között , nincs -10 és -20 között")