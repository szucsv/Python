from mathServices import *
from consolServices import *

money:int=getIntNumber("kerem a toket:")
term:int=getIntNumber("kerem az evek szamat:")
interest:int=getIntNumber("kerem a kamtlábat:")
compoundInterest=compoundInterestCalculator(money,term,interest)

print(f"befektetett osszeg: {money} ft \n Futamido: {term} év \n Kamat: {interest} \n A futamido vegen onnek ennyi penze lesz:{compoundInterest} ft")
