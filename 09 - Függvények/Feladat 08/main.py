from consolServices import *
from lenghtServices import *

length:int=getIntNumberBetweenInterval("Adja meg a telek hosszat:",0,30)
width:int=getIntNumberBetweenInterval("Adja meg a telek szelesseget",0,20)
tax:int=getTax(length, width)

print(f"Az ön telke {length}m hosszu es {width}m szeles az ado pedig {tax}")