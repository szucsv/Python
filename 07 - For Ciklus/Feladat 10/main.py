print("adja meg a kezdoerteket: ", end="")
startValue = int(input())

print("adja meg a vegerteket: ", end="")
endValue = int(input())

sum = 0
product = 1

for i in range(startValue, endValue + 1, 1):
    sum += i
    product *= i

print(f"osszeg: {sum}")
print(f"szorzat: {product}")