from consolServices import *
from paintServices import *

wall:int=getIntNumber()
liter:int=paintCalculator(wall)
price:int=priceCalculator(liter)

print(f"Onnek {liter} festeket kell vennie ami {price}ft")