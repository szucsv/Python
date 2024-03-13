from services import *
from consolServices import *

print("hany forintot szeretne atvaltani?")
huf:int=getIntNumber()
jen:float=hufToJpy(huf)
dollar:float=hufToUsd(huf)
frank:float=hufToChf(huf)

print(f"{jen} jpy")
print(f"{dollar} usd")
print(f"{frank} chf")
JenToEuro=jen*0.0075
DollarToEuro=jen*0.008
FrankToEuro=jen*0.0055
print(f"{JenToEuro} eur")
print(f"{DollarToEuro} eur")
print(f"{FrankToEuro} eur")

