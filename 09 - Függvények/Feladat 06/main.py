from consolServices import *
from schoolServices import *

points: int = getIntNumberBetweenInterval("Hány pontos lett a doga",0,100)
grade: int = calculateGrade(points)

print(f"{grade} értékjegyű lett a doga.")