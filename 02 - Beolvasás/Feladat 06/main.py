print("Megjelenésének éve:",end="")
year:int = int (input())

print("Rendezője neve:" ,end="")
director:str = input()

print("Film címe:" ,end="")
film:str = input()

print("főszereplő neve:" ,end="")
main:str = input()

print(f"{year}-ban {director} rendezésével megjelnt a {film} című film {main} főszereplésével!")