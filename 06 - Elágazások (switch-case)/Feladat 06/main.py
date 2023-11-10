import math
hossz: float = None
szel: float =None
result:float =None
operation:str= None


print("Kérem az oldal hosszát" ,end="")
hossz= int (input())

print("Kérem a téglalap szélességét" ,end="")
szel= int(input())

print("Válasszon egy nűveletet:(t terulet k kerulet a atlo)")
operation = input()

match(operation):
 case"t":
  result=hossz*szel    
 case"k":
    result=2*(hossz+szel)
 case"a":
    result= math.sqrt(hossz*hossz+szel*szel)
 case _:
    print("Nem ertelmezheto")

print(f"A {hossz} hosszúságú és {szel} széleségű téglalap {operation}-e/-ja {result}")
