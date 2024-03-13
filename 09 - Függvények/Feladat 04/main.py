from consolServices import *
from gameServices import*
import random


lownumber:int=inBetween(0,9)
highnumber:int=inBetween(40,50)

randomnum:int=random.randint(lownumber,highnumber)

guess:int=game(randomnum)

print(f"{guess} tippbol talalta ki")