appetizer:str=None
main:str=None
side:str=None
end:str= None
end2:str=None
end3:str=None
error:str=None
result:str=None
print ("Válasszon egy előételt: Zöldségleves,Gyümölcsleves,Húsleves,Nem kérek: ", end="")
appetizer= input().lower()

match(appetizer):
    case"zoldsegleves"|"z"|"zoldseg"|"zöldséleves" |"zöldség":
      end="Zöldségleves"
    case"gyumolcsleves"|"gy"|"gyumolcs"| "gyümölcsleves" |"gyümölcs":
      end="Gyümölcsleves"
    case"husleves"|"h"|"hus"| "húsleves" |"hús":
      end="Húsleves"
    case"nem kerek"|"nem" |"nem kérek":
      end="Nem kért semmit"
    case _:
        error="Nincs ilyen étel"

if(error==None and appetizer=="zoldsegleves" or appetizer=="z" or appetizer=="zoldseg" or appetizer=="zöldséleves" or appetizer=="zöldség" or appetizer=="gyumolcsleves" or appetizer=="gy" or appetizer=="gyumolcs" or appetizer=="gyümölcsleves" or appetizer=="gyümölcs" or appetizer=="husleves" or appetizer=="h" or appetizer=="hus" or appetizer=="húsleves" or appetizer=="hús" or end=="Nem kért semmit" ):
    print(f"{end}-t választott")
else:
    print(f"{error}")







print ("Válasszon egy főételt: Sültcsirkecomb,Sült csirkemell,Rakottzöldség, Spagetti,Pizza,Nem kérek: ", end="")
main= input().lower()

match(main):
    case"sultcsirkecomb"|"sultcsirkec" |"sültcsirkecomb" |"sültcsirkec":
      end2="Sültcsirkecomb"
    case"sült cirkemell"|"sült csirkem"|"sult csirkemell"| "sult csirkem" :
      end2="Sült csirkemell"
    case"rakottzoldseg"|"rakottzold"|"rakottzöldség"| "rakottzöld" :
      end2="Rakottzöldség"
    case"spagetti"|"s" :
      end2="Spagetti"
    case"pizza"|"p" :
      end2="Pizza"
    case"nem kerek"|"nem" |"nem kérek":
      end2="Nem kért semmit"
    case _:
        error="Nincs ilyen étel"

if(error==None and main=="sultcsirkecomb" or main=="sultcsirkec" or main=="sültcsirkecomb" or main=="sültcsirkec" or main=="sült cirkemell" or main=="sült csirkem" or main=="sult csirkemell" or main=="sult csirkem" or main=="rakottzoldseg" or main=="rakottzold" or main=="rakottzöldség" or main=="rakottzöld" or main=="spagetti" or main=="s" or main=="pizza" or main=="p" or end2=="Nem kért semmit" ):
    print(f"{end2}-t választott")
else:
    print(f"{error}")





print ("Válasszon egy köretet: Rizs,Pároltzöldség,Gyümölcs,Sültkrumpli,Saláta,Kóla,Nem kérek: ", end="")
side= input().lower()

match(side):
    case"rizs" | "r":
      end3="Rizs"
    case"paroltzoldseg" | "paroltzold" | "pároltzöldség" | "pároltzöld":
      end3="Pároltzöldség"
    case"gyömolcs" | "gyumolcs" | "gy":
      end3="Gyümölcs"
    case"sültkrumpli" | "sultkrumpli" | "sultk" | "sültk":
        end3="Sültkrumpli"
    case"salata" | "saláta":
        end3="Saláta"
    case"kola" | "kóla" | "k":
        end3="Kóla"
    case"nem kerek" | "nem"  | "nem kérek":
        end3="Nem kért semmit"
    case _:
        error="Nincs ilyen étel"

if(error==None and (side=="rizs" or side=="r" or side=="paroltzoldseg" or side=="paroltzold" or side=="pároltzöldség" or side=="pároltzöld" or side=="gyömolcs" or side=="gyumolcs" or side=="gy" or side=="sültkrumpli" or side=="sultkrumpli" or side=="sultk" or side=="sültk" or side=="salata" or side=="saláta" or side=="kola" or side=="kóla"or side=="k" or end3=="Nem kért semmit")):
    print(f"{end3}-t választott")
else:
    print(f"{error}")

print(f"A mai menü tartalma: {end}, {end2} , {end3}")


if(end=="Húsleves" and end2=="Sült csirkecomb" and end3=="Sültkrumpli" or end3=="Saláta"and(end2!="Pizza" or end2!="Rakottzöldség")):
    result="Vasárnapi menü"
    print(f"A mai menü értékelése: {result}")


elif(end=="Zöldségleves" and end2=="Sült csirkemell" and end3!="Sültkrumpli" and end3=="Rizs"):
    result="Fitnesz menü"
    print(f"A mai menü értékelése: {result}")



elif((end2=="Spagetti" or end2=="Pizza") and (end3=="Gyümölcs" or end3=="Kóla") and end2!="Rakottzöldség" and end3!="Pároltzöldség"):
    result="Napi menü"
    print(f"A mai menü értékelése: {result}")


elif((end!="Nem kért semmit" and end2!="Nem kért semmit" and end3!="Nem kért semmit")or(end=="Zöldségleves" and end2=="Spagetti" and (end3=="Gyümölcs" or end3=="Saláta") and  end2!="Pizza" and  end2!="Rakottzöldség")): 
    result="Kiváló"
    print(f"A mai menü értékelése: {result}")





