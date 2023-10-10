print("Adjon meg az X értékét:", end="")
number:int = int(input())

if(number %2 == 0 ):
    print("BIZ")

elif(number %3 == 0 ):
    print("BAZ") 

elif(number %3 == 0 & number %2 == 0 ):
    print("ZIZI")

else:
    print("")