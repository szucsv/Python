print("Adjon meg egy számot::", end="")
number:int = int(input())

if(number %2 == 0 & number >=0 & number %5 == 0 ):
    print(f"{number} páros, pozitív szám, osztható 5-tel")

elif(number %2 == 0 & number <0 & number %5 == 0 ):
    print(f"{number} páros, negatív szám, osztható 5-tel")

elif(number %2 == 0 & number <0 & number %5 != 0 ):
    print(f"{number} páros, negatív szám, nem osztható 5-tel")


elif(number %2 != 0 & number >=0 & number %5 == 0 ):
    print(f"{number} páratlan, pozitív szám, osztható 5-tel")

elif(number %2 != 0 & number <0 & number %5 == 0 ):
    print(f"{number} páratlan, negatív szám, osztható 5-tel")

elif(number %2 != 0 & number <0 & number %5 != 0 ):
    print(f"{number} páratlan, negatív szám, nem osztható 5-tel")     