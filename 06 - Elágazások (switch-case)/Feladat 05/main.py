numberR1: float = None
numberR2: float = None
type:str = None
result:float = None

print(" Kérem az első ellenállás értékét:", end="")
numberR1 = int (input())

print(" Kérem a második ellenállás értékét:", end="")
numberR2 = int (input())

print("Kérem a bekötés típusát", end="")
type= input().lower()
match(type):
    case"p","parhuzamos",:
     if(numberR1*numberR2==0):
      print("Nem lehet 0-val osztani")
     else:
        result=(numberR1+numberR2)/(numberR1*numberR2)
    case"s,","soros":
     result=numberR1+numberR2
    case _:
        result=None
     
    
if(result == None):
     print("Nem értelmezhető")
else:
    print(f"A {type}-an kapcsolt {numberR1} és {numberR2} ellenállás ertekkel {result} az eredmény ")