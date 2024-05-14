import os
from typing import *
from lottoPlayer import LottoPlayer


def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def convertStringCollectionToIntSet(numbersAsStringCollection:str) -> Set[int]:
    numbersAsIntCollection: Set[int] = set()

    for numberAsString in numbersAsStringCollection.split(","):
        number: int = int(numberAsString)
        numbersAsIntCollection.add(number)

    return numbersAsIntCollection

def getLottoPlayersFromFile(fileName: str) -> List[LottoPlayer]:
    lottoPlayers:List[LottoPlayer] = []
    lottoPlayer: LottoPlayer = None
    oneLine:str = None
    data: List[str] = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")

                lottoPlayer = LottoPlayer()
                lottoPlayer.name = data[0]
                lottoPlayer.tipps = convertStringCollectionToIntSet(data[1])

                lottoPlayers.append(lottoPlayer)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
    except UnicodeDecodeError:
        print("Rossz a kódolása a file-nak!")
    except Exception as ex:
        print("Hiba történt: ", ex)

    return lottoPlayers

def saveWinningNumbersForDay(fileName: str, winningNumbers: Set[int]) -> bool:
    index: int = 1
    
    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for winningNumber in winningNumbers:
                file.write(str(winningNumber))

                if(len(winningNumbers) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False

def saveWinnerNamesForDay(fileName: str, names: List[str]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for name in names:
                file.write(str(name))

                if(len(names) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False
    
def savePlayerNamesWithNumberOfCorrectTipsForDay(fileName: str, winningNumbers: Set[int], lottoPlayers: List[LottoPlayer]) -> bool:
    index: int = 1
    
    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for lottoPlayer in lottoPlayers:
                file.write(f"{lottoPlayer.name} ({lottoPlayer.getNumberOfGoodTips(winningNumbers)})")

                if(len(lottoPlayers) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} mentese sikertelen!")
        return False