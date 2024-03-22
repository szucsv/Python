from consolServices import *
from feleadatServices import*

name:str=getName("kerem a nevet")
hours:int=inBetween(0,77, "kerem a dolgozott orakat")
salary:int=workHours(hours)

print(f"Ön{name} {hours} orat dolgozott ezert {salary} ft fizetest kap")