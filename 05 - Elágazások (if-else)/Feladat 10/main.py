print("Adjon meg az X értékét:", end="")
number:int = int(input())

if(number %3 == 0 & number %2 == 0 ):
    print("ZIZI")
elif(number %3 == 0 ):
    print("BAZ") 
elif(number %2 == 0 ):
    print("BIZ")
else:
    print("Nem osztható 2-vel és 3-al sem")