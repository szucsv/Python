def paintCalculator(wall:int)->int:
        amountPerSquare=wall*0.15
        can:int=0
        if(amountPerSquare % 1 == 0):
            can=amountPerSquare *1
        else:
            while(amountPerSquare %1 != 0):
                amountPerSquare = amountPerSquare-0.01
            can= amountPerSquare + 1 


        return can
def priceCalculator(liter:int)->int:
    price=liter*930
    return price