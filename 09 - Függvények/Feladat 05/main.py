from consolServices import *
from feleadatServices import*
name=getName("kerem a nevet")
salary= workHours()
hours=inBetween(0,77, "kerem a dolgozott orakat")

print(f"Ön{name} {hours} orat dolgozott ezert {salary} ft fizetest kap")