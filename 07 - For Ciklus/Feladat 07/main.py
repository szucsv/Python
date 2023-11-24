startValue:int=None
endValue:int=None

print(" adjon meg egy kezdőértéket:" ,end="")
startValue= int(input())

print("adjon meg egy vég értéket:",end="")
endValue=int(input())

for i in range(endValue,startValue-1,-1):
    print(i)