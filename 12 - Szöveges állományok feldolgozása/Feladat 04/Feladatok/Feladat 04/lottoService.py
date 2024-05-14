from typing import *
import random
from lottoPlayer import LottoPlayer


def generateWinningNumber() -> Set[int]:
    winningNumbers: Set[int] = set()


    while(len(winningNumbers) < 7):
        winningNumbers.add(random.randint(1, 45))

    return winningNumbers

def printLottoPlayersToConsole(lottoPlayers: List[LottoPlayer]) -> None:
    for lottoPlayer in lottoPlayers:
        print(str(lottoPlayer))

def printFileOperationResultToConsole(fileName: str, fileWriteSucceeded: bool) -> None:
    if(fileWriteSucceeded):
        print(f"{fileName} allomany letrehozva")
    else:
        print(f"{fileName}allomany nem lett letrehozva")

def getLottoWinners(lottoPlayers: List[LottoPlayer], winningNumbers: Set[int]) -> List[str]:
    lottoWinners: List[str] = []

    for lottPlayer in lottoPlayers:
        if(lottPlayer.hasWiningTicket(winningNumbers)):
            lottoWinners.append(lottPlayer.name)

    return lottoWinners