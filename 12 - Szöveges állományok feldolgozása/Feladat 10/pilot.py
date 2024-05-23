import datetime

class Pilot:
    def __init__(self) -> None:
        self.name: str = None
        self.birtdate: datetime = None
        self.nationality: str = None
        self.startNumber: int = None

    def __str__(self) -> str:
        return f"{self.startNumber} {self.name}\n{self.nationality}\t{self.birtdate})"