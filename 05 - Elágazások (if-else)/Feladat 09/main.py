print("Adjon meg az X értékét:", end="")
numberx:int = int(input())

print("Adjon meg az Y értékét:", end="")
numbery:int = int(input())

if(numberx %numbery == 0 ):
    print(f"Y oszója x-nek")

else:
    print(f"Y nem oszója x-nek")