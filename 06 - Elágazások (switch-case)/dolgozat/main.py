tem:float=None
switch:str=None
end:float=None
error:str=None
print("Adja meg a hőmérsékletet(°C):" , end="")
tem= float(input())

print("°F,vagy °K legyen az átváltás mértékegysége?", end="")
switch=input()

match(switch):
    case "f"|"F":
     end=(tem-32)/1.8
    case "k"|"K":
     end=tem+273.15
    case _:
        error=("nincs ilyen atvaltas")

if(switch=="f"or switch=="F"):
 print(f"{tem}°C = {end}°F")
elif(switch=="k" or switch=="K"):
 print(f"{tem}°C = {end}°K")
else:
 print(f"{error}")