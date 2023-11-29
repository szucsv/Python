print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

for i in range(startValue, endValue + 1, 1):
    if( i % 2 == 1):  
        print(i)