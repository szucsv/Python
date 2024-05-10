class Settlement:
    def __init__(self) -> None:
        self.name:str = None
        self.type:str = None
        self.county:str = None
        self.countyDistrict:str = None
        self.microRegion:str = None
        self.population:int = None
        self.area:float = None
    
    def __str__(self) -> str:
        return f"Városnév: {self.name}\nTípus: {self.type}\nMegye: {self.county}\nJáras: {self.countyDistrict}\nKistérség: {self.microRegion}\nNépesség: {self.population}\nTerület: {self.area}\n"