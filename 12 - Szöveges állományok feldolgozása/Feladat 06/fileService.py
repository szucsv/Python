import datetime
import os
from typing import *

from footballPlayer import FootballPlayer

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getFootballPlayersFromFile(fileName: str) -> List[FootballPlayer]:
    footballPlayers:List[FootballPlayer] = []
    footballPlayer: FootballPlayer = None
    oneLine:str = None
    data: List[str] = None


    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8-sig', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")

                footballPlayer = FootballPlayer()
                footballPlayer.team = data[0]
                footballPlayer.jarsey = int(data[1])
                footballPlayer.firstName = data[2]

                if(len(data) == 9):
                    footballPlayer.lastName = data[3]
                    footballPlayer.birthDate = datetime.datetime.strptime(data[4], '%Y.%m.%d.').date()
                    footballPlayer.isHungarianCitizen = int(data[5]) == -1 if True else False
                    footballPlayer.isForeignCitizen = int(data[6]) == -1 if True else False
                    footballPlayer.worth = int(data[7])
                    footballPlayer.position = data[8]

                    footballPlayer.isGoalKeeper = data[8] == "kapus"

                else:
                    footballPlayer.birthDate = datetime.datetime.strptime(data[3], '%Y.%m.%d.').date()
                    footballPlayer.isHungarianCitizen = int(data[4]) == -1 if True else False
                    footballPlayer.isForeignCitizen = int(data[5]) == -1 if True else False
                    footballPlayer.worth = int(data[6])
                    footballPlayer.position = data[7]

                    footballPlayer.isGoalKeeper = data[7] == "kapus"

                footballPlayers.append(footballPlayer)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return footballPlayers

def writeFootballPlayersToFile(fileName: str, footballPlayers: Dict[str, List[FootballPlayer]]) -> bool:
    index: int = 1

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="w+") as file:
            for team, players in footballPlayers.items():
                file.write(f"{team}:\n")

                for player in players:
                    file.write(f"\t- {player.firstName} {player.lastName} - {player.position} - (${player.worth}):\n")
                
                if(len(footballPlayers) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")
        return False