import os
import time
#válzozók definiálása
#a szám , amit be kell olvasni
#kezdőértéke None, mivel a while-ciklusban ki tudom ezt hasznalni az ismetlesek vizsgalatara
#vagyis a ciklust mindaddig futtatjuk, amíg a number változónak nem lesz szám értéke
number:int = None
data:str="" # segédváltozó , a beolvasott értékét fogja tarolni
#a while ciklus, ami mindaddig fog futni, amíg a number változo nem kap szám értéket,azaz az értéke nem None lesz
while(number==None or(number<0 or number>9)):
    # beolvasás a konzolrol es a beolvasott erteket eltaroljuk
    data=input("kérem a szamot: ")
    #megvizsgaljuk , hogy a beolvasott ertek string szamra alakithato-e
    #mindegy  hogy ez a szam int vagy float tipusu
    #idigit() -> bool valtozo ad vissza
    isNumber:bool = data.replace("-","").isdigit()
    if(not isNumber):
        number = int(data)
    elif(isNumber and (number< 0 or number>9)):
        print("Nem szamot adott meg")
        #ha az isdigit() fuggveny erteke igaz akkor szamot ir be a felhasznalo
        #amit mi biztos at tudunk szam tipusava alakitani
        number = int(data)

#az isdigit() fuggveny erteke hamis azaz a felhasznalo nem szamot irt be
#igy a number valtozo erteke tovabbra is None marad, azaz a felhasznalo nem szamot irt be
#a ciklust ismetelni kell
    else:
        print("\nNem szamot adott meg!")


        # a programot futtato szalat (thread) elaltatjuk harom masodpercre
        time.sleep(3)

    #letoroljuk a kepernyot
    os.system("cls")

    #egy vegtelen while ciklust irunk, mivel arra fogunk varni, hogy a felhasznalo
    # lenyomja a kert billentyut (ENTER)

#kiirjuk a beolvasott szamot
print(f" a beolvasott szam {number}")


