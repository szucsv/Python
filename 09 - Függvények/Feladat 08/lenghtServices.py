
def getTaxRate(length:int,width:int) -> int :
    taxRate:int=0
    if(length<30 and width<20):
        taxRate=0.75
    else:
        taxRate=1

def getTaxValue(quater,taxRate,price=1000)-> float:
    tax=quater*taxRate*price

def getTax(width,length,quater)->float:
        quater=width*length
        TaxRate:getTaxRate(width,length)
        tax:getTax(quater,TaxRate)
        return tax
