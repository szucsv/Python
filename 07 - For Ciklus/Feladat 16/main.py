sumeven:int = 0
summodd:int = 0
avarage:float = 0

print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())

for i in range(startValue,endValue+1,1):
    if i % 2 == 0:
        sumeven += i
    else:
        summodd += i

avarage=(sumeven+summodd)/2
print(f"{avarage}")