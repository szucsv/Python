def convertFromCelsius(celsius:float,convertTo:str)-> float:

    convertedResult:float=None

    match(convertTo.lower()):
        case"k":convertedResult=celsius+273.15
        case"f":convertedResult=((9/5)*celsius)+32
        #ha a convertTo nem K vagy F akkor hibat dobunk
        case _:raise Exception('Noncs olyan mertekegyseg amire atalakitani kivanja!')
        

    return convertedResult

def compoundInterestCalculator(money:int,term:int,interest:int)-> float:
    compoundInterest:int=None
    compoundInterest=money*(1+(term/12))*(12*term)
    
    return compoundInterest
