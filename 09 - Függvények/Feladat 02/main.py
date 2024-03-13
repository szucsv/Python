from consolServices import *
from mathServices import *
from point import Point

pointA:Point=Point()
pointA.X=getFloatNumber("Adja meg az A pont X kordinatajat")
pointA.Y=getFloatNumber("Adja meg az A pont Y kordinatajat")

pointB:Point=Point()
pointB.X=getFloatNumber("Adja meg az B pont X kordinatajat")
pointB.Y=getFloatNumber("Adja meg az B pont Y kordinatajat")

distance:float=calculatePointDistance(pointA,pointB)

print(f"A[{pointA.X,pointA.Y}]-B[{pointB.X,pointB.Y}]={distance}")