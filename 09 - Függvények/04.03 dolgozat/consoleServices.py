def getIntNum(prompt:str)->int:
    
    num:int=None
    data:str=""

    while(num==None):
        print(f"{prompt}",end="")
        data=input()
        isNumber:bool=data.isdigit

        if(isNumber):
            num=int(data)
        else:
            print("nem szamot adott meg")
    return num

def getFloatNum(prompt:str)->float:
    
    num:float=None
    data:str=""

    while(num==None):
        print(f"{prompt}",end="")
        data=input()
        isNumber:bool=data.replace("-","",1).replace(",","",1).replace(".","",1).isdigit

        if(isNumber):
            num=float(data)
        else:
            print("nem szamot adott meg")
    return num