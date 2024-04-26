class Student:
    def __init__(self):
        self.name:str=None
        self.avarage:float=0

    def getCategory(self)->str: 
        category:str="kitűnő"

        if (self.avarage>=4 and self.avarage<5):
            category="jeles"
        elif (self.avarage>=3 and self.avarage<4):
            category="jó"
        elif (self.avarage>=2 and self.avarage<3):
            category="elégséges"
        elif(self.avarage>=1 and self.avarage<2):
            category="elégtelen"

        return category

    def __str__(self) -> str:
        return f"{self.name}:{self.avarage}"