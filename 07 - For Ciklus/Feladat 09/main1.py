print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

if (endValue % 2==1):
    endValue -= 1

for i in range(endValue,startValue-1,-2):
    print(i)