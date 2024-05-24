class Physicist:
    def __init__(self) -> None:
        self.year: int = None
        self.type: str = None
        self.firstName: str = None
        self.lastName: str = None

    def getFullName(self) -> str:
        if(self.lastName != None):
            return f"{self.firstName} {self.lastName}"
        else:
            return f"{self.firstName}"
    
    def __str__(self) -> str:
        return f"{self.year}: {self.firstName} {self.lastName} ({self.type})"