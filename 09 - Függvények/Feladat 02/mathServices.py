from point import Point
from math import sqrt
def convertFromCelsius(celsius:float,convertTo:str)-> float:

    convertedResult:float=None

    match(convertTo.lower()):
        case"k":convertedResult=celsius+273.15
        case"f":convertedResult=((9/5)*celsius)+32
        #ha a convertTo nem K vagy F akkor hibat dobunk
        case _:raise Exception('Noncs olyan mertekegyseg amire atalakitani kivanja!')
        

    return convertedResult

def calculatePointDistance(pointA:Point,pointB:Point) ->float:
    distance:float=0

    x:float= abs(pointB.X- pointA.X)
    y:float=(pointB.Y- pointA.Y)

    distance=sqrt(x**2 + y**2)

    return distance