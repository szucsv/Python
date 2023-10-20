month:int = None
output:str= None
error:str= None

print(f"Kérem a hónap nevet:" , end="")
month = input().lower()

match(month):
    case "januar":
        output=1
    case 2:
        output="februar"
    case "marcius":
        output=3
    case "aprilis":
        output=4
    case "majus":
        output=5
    case "junius":
        output=6
    case "julius":
        output=7
    case "augusztus":
        output=8
    case "szeptember":
        output=9
    case "oktober":
        output=10
    case "november":
        output=11
    case "december":
        output=12
    case _:

        error ="nincs ilyen honap"

if(error == None and output >= 1 and output <= 12):
    print(f" {output} az év  {month}. hónapja")
elif(error != None):
    print(error)    