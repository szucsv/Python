from consolServices import *
from mathServices import convertFromCelsius

celsius:float = getFloatNumber("Adja meg a homersekletet celsiusban")
convertTo:str=oneSpecificLetter("Adja meg az atvaltas tipusat",["F","f","K","k"])
convertedResult=convertFromCelsius=(celsius,convertTo)

print(f"{celsius} C = {convertedResult:1.2f}{convertTo.upper()}")