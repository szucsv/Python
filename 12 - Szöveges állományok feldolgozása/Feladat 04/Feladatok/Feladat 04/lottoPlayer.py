from typing import List, Set

class LottoPlayer:
    def __init__(self) -> None:
        self.name:str = None
        self.tipps:Set[int] = None

    def getNumberOfGoodTips(self, winningNumbers: Set[int]) -> int:
        numberOfGoodTips: int = len(set(self.tipps).intersection(winningNumbers))
        return numberOfGoodTips

    def hasWiningTicket(self, winningNumbers: List[int]) -> bool:
        numberOfGoodTips: int = self.getNumberOfGoodTips(winningNumbers)
        return numberOfGoodTips == 7
    
    def __str__(self) -> str:
        return f"{self.name}\t\t{self.tipps}"