import os
import time

name:str=None
areAllLettersInString:bool = False

os.system("cls")


while (name == None or len(name) <2 or not name.isalpha()):
    print("Adja meg a nevet: ")
    name = input()

    areAllLettersInString = name.isalpha
    
    if(areAllLettersInString and len(name)<2):
        print("lealabb 2 karakternek kell lennie")

    if(not areAllLettersInString):
        print("A nevben csak betuk lehetnek")
os.system("cls")


print(f"udvozoljuk {name}!")