import random
def generateRandomNumber()  -> int:
    randomValue = random.uniform(350, 400)
    return randomValue

def hufToJpy(amountInHuf) ->float:
    amount_in_jpy = amountInHuf * 0.41
    return amount_in_jpy

def hufToUsd(amountInHuf) -> float:
    amount_in_usd = amountInHuf * 0.0028
    return amount_in_usd

def hufToChf(amountInHuf) ->float:
    amountInChf = amountInHuf * 0.0024
    return amountInChf
