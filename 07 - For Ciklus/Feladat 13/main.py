even=0
odd=0

print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())
for i in range(startValue,endValue+1,1):
    if(startValue%2 ==0):
        even += i
    else:
        odd += i

if(even>odd):
    print(f"parosbol van tobb")
elif(even<odd):
    print(f"parosbol van tobb")
else:
    print(f"egyenloek")
    