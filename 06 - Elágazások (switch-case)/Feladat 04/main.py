numberOne: float = None
numberTwo: float = None
operationType: str = None
result:float = None

print("Kérem az első számot:" ,end="")
numberOne = float(input())

print("Kérem az második számot:" ,end="")
numberTwo = float(input())

print("Kérem a műveletet:" ,end="")
operationType = input()
if(numberTwo== 0 and operationType == "/"):
    print("0-val nem lehet osztani!")
    quit()
    
match(operationType):
 case"-":
    result = numberOne - numberTwo
 case"+":
    result = numberOne + numberTwo
 case"*":
    result = numberOne * numberTwo
 case"/":
    result = numberOne / numberTwo
 case"_":
    result = None

if(result==None):
    print("Nem letezo muveletet valasztott!")
else:
    print(f"{numberOne} {operationType} {numberTwo} = {result}")