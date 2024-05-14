from typing import *

class VolleyballTeam:
    def __init__(self) -> None:
        self.name:str = None
        self.points:List[int] = []

    def getNumberOfTieMatches(self) -> int:
        return self.points.count(2)
    
    def getNumberOfMatchesWithFiveSets(self) -> int:
        return self.points.count(1)
    
    def getSumOfPoints(self) -> int:
        sum: int = 0

        for point in self.points:
            sum += point

        return sum
    
    def getWinningPercent(self) -> float:
        winPoints: int = self.points.count(3) * 3
        allpoints: int = self.getSumOfPoints()
        return (winPoints * 100) / allpoints
    
    def getLoosePercent(self) -> float:
        return 100 - self.getWinningPercent()

    def __str__(self) -> str:
        return f"{self.name}\t\t{self.points}"