

def bmiCalculator(height:float,weight:int)->float:
    bmi=weight/(height*height)

    return bmi

def healthBmiCalculator(bmi:bool)-> int:
    helathStatus:str=None
    if(bmi<18.5):
        helathStatus="Sovány"
    elif(bmi>18.5 and bmi<25):
        helathStatus="Normál testsúly"
    elif(bmi>25 and bmi<30):
        helathStatus="Túlsúly"
    elif(bmi>30):
        helathStatus="Elhízott"

    return helathStatus