startValue = 0
endValue = 0
count = 0

print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())

if (startValue % 2 == 0):
    startValue += 1


for i in range(startValue,endValue+1,2):
    if( i % 3 == 0):
        count += 1
print(f"{count}")