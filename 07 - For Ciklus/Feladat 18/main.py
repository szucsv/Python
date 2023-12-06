sum:int=0
multyply:int=1


print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())

for i in range(startValue,endValue+1,1):
    sum+=i*multyply
    multyply *=-1

print(f"{sum}")