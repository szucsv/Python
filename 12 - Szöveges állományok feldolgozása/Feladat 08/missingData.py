class MissingData:
    def __init__(self) -> None:
        self.name: str = None
        self.grade: str = None
        self.firstDay: int = None
        self.lastDay: int = None
        self.missedHours: int = None
    
    def __str__(self) -> str:
        return f"{self.name} ({self.grade})\n{self.firstDay} - {self.lastDay} ({self.missedHours})"