import os  
import time

name : str = None


while(name == None):
    print("Kérem a nevét: ",end="")
    name=input()

    isName : bool = name.isalpha()
    if (isName and len(name) < 2):
        print("Nem nevet adott meg")
        time.sleep(3)
        os.system("cls")
    elif(not isName):
        print("Szam van benne")
        time.sleep(3)
        os.system("cls")
    else:
        break

print(f"Hello {name.capitalize()} !")

#name:str=None
#areAllettersinString:bool = False

#os.system(cls)

#while (name == None or len(name) <2 or notname.isalpha()):
    #print("Adja meg a nevet: ")
    #name = input()

    #if(len(name)<2):
        #print("lealabb 2 karakternek kell lennie")

    #if(not areAlllettersInString):
        #print("A nevben csak betuk lehetnek")
#os.system(cls)

#print(f"udvozoljuk{name}!")