print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

if (startValue % 2==0):
    startValue += 1

for i in range(startValue,endValue,2):
    print(i)