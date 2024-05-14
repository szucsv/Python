from typing import *
from volleyballTeam import VolleyballTeam

def printTeamsNumberOfTieMatch(volleyballTeams:List[VolleyballTeam]) -> None:
    for volleyballTeam in volleyballTeams:
        print(f"{volleyballTeam.name} {volleyballTeam.getNumberOfTieMatches()}")

def printTeamsNumberOfFiveSetMatch(volleyballTeams:List[VolleyballTeam]) -> None:
    for volleyballTeam in volleyballTeams:
        print(f"{volleyballTeam.name} {volleyballTeam.getNumberOfMatchesWithFiveSets()}")

def orderTeamsByPointsDescending(volleyballTeams:List[VolleyballTeam]) -> None:
    temp: VolleyballTeam = None
    
    for i in range (0, len(volleyballTeams) - 1, 1):
        for j in range(i + 1, len(volleyballTeams), 1):
            if(volleyballTeams[j].getSumOfPoints() > volleyballTeams[i].getSumOfPoints()):
                temp = volleyballTeams[i]
                volleyballTeams[i] = volleyballTeams[j]
                volleyballTeams[j] = temp

def printIndexedTeamsToConsole(volleyballTeams:List[VolleyballTeam]) -> None:
    for index, volleyballTeam in enumerate(volleyballTeams):
        print(f"{index} - {volleyballTeam.name}\t{volleyballTeam.getSumOfPoints()}")

def printWinAndLossRatio(volleyballTeams:List[VolleyballTeam]) -> None:
    for volleyballTeam in volleyballTeams:
        print(f"{volleyballTeam.name} : \t\tW: {volleyballTeam.getWinningPercent()}%\t\tL: {volleyballTeam.getLoosePercent()}%")

def getWinRatioAvaraga(volleyballTeams:List[VolleyballTeam]) -> float:
    avarageSum: float = 0

    for volleyballTeam in volleyballTeams:
        avarageSum += volleyballTeam.getWinningPercent()

    return avarageSum / len(volleyballTeams)

def getTemsUnderAvarageWiningRatio(volleyballTeams:List[VolleyballTeam]) -> List[VolleyballTeam]:
    teamsUnderAvarageRatio: List[VolleyballTeam] = []
    winRatioAvaraga: float = getWinRatioAvaraga(volleyballTeams)

    for volleyballTeam in volleyballTeams:
        if(volleyballTeam.getWinningPercent() < winRatioAvaraga):
            teamsUnderAvarageRatio.append(volleyballTeam)

    return teamsUnderAvarageRatio

def printTemsUnderAvarageWiningRatioToConsole(volleyballTeams:List[VolleyballTeam]) -> None:
    for volleyballTeam in volleyballTeams:
        print(f"{volleyballTeam.getWinningPercent():.2f}% - {volleyballTeam.name}")