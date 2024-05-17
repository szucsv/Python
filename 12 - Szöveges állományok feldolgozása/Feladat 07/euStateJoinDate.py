import datetime


class EuStateJoinDate:
    def __init__(self) -> None:
        self.state: str = None
        self.joinDate: datetime.date = None

    def __str__(self) -> str:
        return f"{self.state} ({self.joinDate.year}-{self.joinDate.month}-{self.joinDate.day})"