from consolServices import *
hours:int=None
name:str=""
overWork:int=None
def workHours()->int:
    while(hours==None or (hours>77 or hours)):
        hours=getIntNumber("kerem a szamot")
        if( hours>40):
            overWork=hours-40
        elif(hours>77):
            print("nem  dolgozhat ennyit")
        elif(hours==0):
            print("nem dolgozott")
        elif(hours<40):
            overWork=0

        salary=overWork*1500+(hours-overWork)*1000
    return salary

