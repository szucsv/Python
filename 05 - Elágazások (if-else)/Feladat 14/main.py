print("Adjon meg egy számot:", end="")
numberx:int = int(input())

print("Adjon meg egy másik számot:", end="")
numbery:int = int(input())

print("Adjon meg egy harmadik számot:", end="")
numberz:int = int(input())

if(numberx %numbery == 0 ):
    print(f"{numberx} osztható {numbery}-nal")

elif(numberx %numberz == 0 ):
    print(f"{numberx} osztható {numberz}-vel")

elif(numberx %numberz == 0 & numberx %numbery == 0  ):
    print(f"{numberx} osztható {numberz}-vel és {numbery}-nal is")

