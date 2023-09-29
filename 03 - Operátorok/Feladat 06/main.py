print("y =" , end="")
y:float = float(input())
y+=0.5

print("z =" , end="")
z:float = float(input())
z-=0.7

print("s =" , end="")
s:float = float(input())

eredmeny:float = (y*z)/s

print(f"({y} * {z}) / {s} = {eredmeny}")