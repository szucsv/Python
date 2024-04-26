class City:
    def __init__(self):
        self.name: str = None
        self.type: str = None
        self.county: str = None
        self.district: str = None
        self.smallarea: str = None
        self.population: int = 0
        self.zone: float = 0
        
    def __str__(self) -> str:
        return f"{self.name} {self.type} {self.county} {self.district} {self.smallarea} {self.population} {self.zone}"