import datetime


class FootballPlayer:
    def __init__(self) -> None:
        self.team:str = None
        self.jarsey:int = None
        self.firstName: str = None
        self.lastName: str = None
        self.birthDate: datetime = None
        self.isHungarianCitizen: bool = False
        self.isForeignCitizen: bool = False
        self.worth: int = None
        self.position: str = None
        self.isGoalKeeper: str = False

    def __str__(self) -> str:
        return f"{self.name}\t\t{self.points}"