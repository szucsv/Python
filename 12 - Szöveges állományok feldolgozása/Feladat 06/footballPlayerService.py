import datetime
from typing import Dict, List, Set

from citizenships import Citizenships
from footballPlayer import FootballPlayer

def printFileResultToConsole(fileName: str, fileWriteSucceeded: bool) -> None:
    if(fileWriteSucceeded):
        print(f"{fileName} allomany letrehozva")
    else:
        print(f"{fileName}allomany nem lett letrehozva")

def orderTeamsByBirthdateDescending(footballPlayers:List[FootballPlayer]) -> None:
    temp: FootballPlayer = None
    
    for i in range (0, len(footballPlayers) - 1, 1):
        for j in range(i + 1, len(footballPlayers), 1):
            if(footballPlayers[j].birthDate.year > footballPlayers[i].birthDate.year):
                temp = footballPlayers[i]
                footballPlayers[i] = footballPlayers[j]
                footballPlayers[j] = temp

def getOldestFeildPlayer(footballPlayers:List[FootballPlayer]) -> FootballPlayer:
    oldestFootballPlayer: FootballPlayer = None

    orderTeamsByBirthdateDescending(footballPlayers)

    for footballPlayer in footballPlayers:
        if (not footballPlayer.isGoalKeeper):
            oldestFootballPlayer = footballPlayer
            break

    return oldestFootballPlayer

def getPlayersCitizenship(footballPlayers:List[FootballPlayer]) -> Citizenships:
    citizenships: Citizenships = Citizenships()

    for footballPlayer in footballPlayers:
        if(footballPlayer.isHungarianCitizen and footballPlayer.isForeignCitizen):
            citizenships.both += 1
        elif(footballPlayer.isHungarianCitizen):
            citizenships.onlyHungarian += 1
        elif(footballPlayer.isForeignCitizen):
            citizenships.onlyForegin += 1

    return citizenships

def getTeamNames(footballPlayers:List[FootballPlayer]) -> Set[str]:
    teams:Set[str] = set()

    for footballPlayer in footballPlayers:
        teams.add(footballPlayer.team)

    return teams

def getFieldNames(footballPlayers:List[FootballPlayer]) -> Set[str]:
    fields:Set[str] = set()

    for footballPlayer in footballPlayers:
        fields.add(footballPlayer.position)

    return fields

def getPlayersValueByTeams(footballPlayers:List[FootballPlayer]) -> Dict[str, int]:
    playersValueByTeams: Dict[str, int] = {}

    teamNames:Set[str] = getTeamNames(footballPlayers)
    for teamName in teamNames:
        playersValueByTeams[teamName] = 0

    for footballPlayer in footballPlayers:
        playersValueByTeams[footballPlayer.team] += footballPlayer.worth

    return playersValueByTeams

def getPlayersByTeam(footballPlayers:List[FootballPlayer]) -> Dict[str, List[FootballPlayer]]:
    playersByTeam :Dict[str, List[FootballPlayer]] = {}  

    teams:Set[str] = getTeamNames(footballPlayers)
    for team in teams:
        playersByTeam[team] = []

    for footballPlayer in footballPlayers:
        playersByTeam[footballPlayer.team].append(footballPlayer)

    return playersByTeam                                            

def printPlayersValueByTeams(playersValueByTeams: Dict[str, int]) -> None:
    for team, value in playersValueByTeams.items():
        print(f"{team} jatekosainak ossz erteke ${value}")

def getTeamsWhereOnlyOnePlayerIsOnPosition(footballPlayers:List[FootballPlayer]) -> Dict[str, List[str]]:
    teamsWhereOnlyOnePlayerIsOnPosition: Dict[str, List[str]] = {}
    counter: int = 0

    playersByTeam :Dict[str, List[FootballPlayer]] = getPlayersByTeam(footballPlayers)
    fields:Set[str] = getFieldNames(footballPlayers)
    teams:Set[str] = getTeamNames(footballPlayers)

    for team in teams:
        teamsWhereOnlyOnePlayerIsOnPosition[team] = []
    
    for team, players in playersByTeam.items():
        
        for field in fields:
            for player in players:
                if(field == player.position):
                    counter += 1
            
            if(counter == 1):
                teamsWhereOnlyOnePlayerIsOnPosition[team].append(field)

            counter = 0

    return teamsWhereOnlyOnePlayerIsOnPosition

def printTeamsWhereOnlyOnePlayerIsOnPosition(teamsWhereOnlyOnePlayerIsOnPosition: Dict[str, List[str]]) -> None:
    for team, positions in teamsWhereOnlyOnePlayerIsOnPosition.items():
        print(f"{team} :")
        for position in positions:
            print(f"- {position}")

def getSumOfPlayerWorth(footballPlayers:List[FootballPlayer]) -> int:
    sum: int = 0

    for footballPlayer in footballPlayers:
        sum += footballPlayer.worth

    return sum

def getPlayersUnderAvarageWorth(footballPlayers:List[FootballPlayer]) -> List[FootballPlayer]:
    playersUnderAvarageWorth: List[FootballPlayer] = []

    sumOfPlayerWorth: int = getSumOfPlayerWorth(footballPlayers)
    avarageWoth: float = sumOfPlayerWorth / len(footballPlayers)

    for footballPlayer in footballPlayers:
        if(footballPlayer.worth < avarageWoth):
            playersUnderAvarageWorth.append(footballPlayer)

    return playersUnderAvarageWorth

def printPlayersUnderAvarageWorth(playersUnderAvarageWorth: List[FootballPlayer]) -> None:
    for footballPlayer in playersUnderAvarageWorth:
        print(f"{footballPlayer.firstName} {footballPlayer.lastName} (${footballPlayer.worth})")

def getHungarianPlayersBetween18And21Age(footballPlayers:List[FootballPlayer]) -> List[FootballPlayer]:
    hungarianPlayersBetween18And21Age: List[FootballPlayer] = []
    currentYear: int =  datetime.datetime.now().year
    
    for footballPlayer in footballPlayers:
        age: int = currentYear - footballPlayer.birthDate.year
        if(footballPlayer.isHungarianCitizen and (age >= 18 and age <= 21)):
            hungarianPlayersBetween18And21Age.append(footballPlayer)

    return hungarianPlayersBetween18And21Age

def printHungarianPlayersBetween18And21Age(footballPlayers:List[FootballPlayer]) -> None:
    if(len(footballPlayers) == 0):
        print("\nNincs 18 és 21 év közti amagyar állampolgársagu jatekos")
        return
    
    for footballPlayer in footballPlayers:
        print("\n18 és 21 év közti amagyar állampolgársagu jatekos")
        print(f"{footballPlayer.firstName} {footballPlayer.lastName} (${footballPlayer.worth}), {footballPlayer.team}")

def getPlayersWithHungarianCitizenship(footballPlayers:List[FootballPlayer]) -> Dict[str, List[FootballPlayer]]:
    playersWithHungarianCitizenship: Dict[str, List[FootballPlayer]] = {}

    teams:Set[str] = getTeamNames(footballPlayers)
    for team in teams:
        playersWithHungarianCitizenship[team] = []

    for footballPlayer in footballPlayers:
        if(footballPlayer.isHungarianCitizen and not footballPlayer.isForeignCitizen):
            playersWithHungarianCitizenship[footballPlayer.team].append(footballPlayer)

    return playersWithHungarianCitizenship

def getPlayersWithForeignCitizenship(footballPlayers:List[FootballPlayer]) -> Dict[str, List[FootballPlayer]]:
    playersWithForeignCitizenship: Dict[str, List[FootballPlayer]] = {}

    teams:Set[str] = getTeamNames(footballPlayers)
    for team in teams:
        playersWithForeignCitizenship[team] = []

    for footballPlayer in footballPlayers:
        if(footballPlayer.isForeignCitizen and not footballPlayer.isHungarianCitizen):
            playersWithForeignCitizenship[footballPlayer.team].append(footballPlayer)

    return playersWithForeignCitizenship