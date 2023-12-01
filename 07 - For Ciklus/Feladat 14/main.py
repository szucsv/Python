five=0
seven=0

print("kerem a kezdoerteket:", end="")
startValue = int(input())

print("kérem a vegerteket:", end="")
endValue = int(input())
for i in range(startValue,endValue+1,1):
    if(i%7 ==0 and i%5 ==0):
        five += i  
        seven += i
    elif(i%5 ==0):
        five += i
    elif(i%7 ==0):
        seven += i
    
if(five>seven):
    print(f"ottel oszthato szamok osszege a nagyobb")
elif(five<seven):
    print(f"hettel oszthato szamok osszege a nagyobb")
elif(five==seven):
    print(f"egyenloek")