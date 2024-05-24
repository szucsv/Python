from nobel import*
from typing import*
from fileService import*


def getMcType(nobels:List[Nobel])->str:
    for nobel in nobels:
        if(nobel.surname=="Arthur B." and nobel.firstName=="McDonald"):
            return nobel.type

def getLiterary2017(nobels:List[Nobel])->str:
    names:str=None
    for nobel in nobels:
        if(nobel.year==2017 and nobel.type=="irodalmi"):
            names=f"{nobel.surname} {nobel.firstName}"
            return names

def getOrganizationsFrom1990(nobels:List[Nobel])->Dict[int,str]:
    yearAndOrganization:Dict[int,str]={}

    for nobel in nobels:
        if(nobel.firstName==""and nobel.year>=1990 and nobel.type=="béke"):
            yearAndOrganization[nobel.year]+=nobel.surname
    
    return yearAndOrganization

def printRecent(yearAndOrganization:Dict[int,str])->None:
    for year, organization in yearAndOrganization.items():
        print(f"\t {year}: {organization}")

def getCuries(nobels:List[Nobel])->List[str]:
    curies:List[str]=[]
    for nobel in nobels:
        if(nobel.firstName=="Curie"):
            curies.append(nobel)
    
    return curies
