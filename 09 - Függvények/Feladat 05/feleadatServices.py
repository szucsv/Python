from consolServices import *

def workHours(hours:int)->int:
    overWork:int=None
    salary:int=None

    if( hours>40):
        overWork=hours-40
    elif(hours>77):
        print("nem  dolgozhat ennyit")
    elif(hours==0):
        print("nem dolgozott")
    elif(hours<=40):
        overWork=0

    salary=overWork*1500+(hours-overWork)*1000
    return salary

