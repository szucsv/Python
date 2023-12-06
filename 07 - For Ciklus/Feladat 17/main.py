sum:int = 0
devide:float = 0
count:int = 0

print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())

for i in range(startValue,endValue+1,1):
    count+=1
    sum+=i

devide=sum/count

print(f"{devide}")
