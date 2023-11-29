print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

summary = 0
product = 1

for i in range(startValue, endValue + 1, 1):
    summary = summary + i
    product = product * i
    print(i)

print(f"osszege: {summary}")
print(f"szorata: {product}")