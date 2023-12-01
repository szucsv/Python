print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())

sum:int = 0
product:int = 1

for i in range(startValue,endValue + 1,1):
    if(i % 2 == 0):
        sum +=i
    elif(i % 2 != 0):
        product *=i
print(sum)
print(product)