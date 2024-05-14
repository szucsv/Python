from typing import *
from fileService import *
from volleyballTeamService import *

#0
volleyballTeams:List[VolleyballTeam] = getVolleyballTeamsFromFile("adatok.txt")

#1
# Hány csapat vett részt a bajnokságban?
print(f"\nA bajnoksagban {len(volleyballTeams)} csapat vett reszt")

#2
# Döntetlen mérkőzéskor a csapat 2 pontot szerez. Mutassa be csapatonként ki hány döntetlen mérkőzést játszott le!
print("\nCsapatonként döntetlen mérkőzések száma:")
printTeamsNumberOfTieMatch(volleyballTeams)

#3
# Ha egy mérkőzés 5 szetben dől el, akkor a vesztes csapat 1 pontot szerez.
# Mely csapatok játszottak 5 szettes mérkőzést és hányat?
print("\nCsapatonként az 5 szettes mérkőzések száma:")
printTeamsNumberOfFiveSetMatch(volleyballTeams)

#4
# Ki a  bajnogság első három helyezete. Mutassa be mintának megfelelően:
# helyezés - csapat neve		pontszám
orderTeamsByPointsDescending(volleyballTeams)
top3: List[VolleyballTeam] = volleyballTeams[:3]
print("\nAz elso három csapat:")
printIndexedTeamsToConsole(top3)

#5
# Az elért pontok alapján, az utolsó három csapat kiesik az első osztályból.
# Kik ők?
last3: List[VolleyballTeam] = volleyballTeams[-3:]
print("\nAz utolsó három csapat:")
printIndexedTeamsToConsole(last3)

#6
# Mutassa be csapatonként a győzelmi és verességi arányt csapatonként!
teamsUnderAvarageRatio: List[VolleyballTeam] = getTemsUnderAvarageWiningRatio(volleyballTeams)
winRatioAvaraga: float = getWinRatioAvaraga(volleyballTeams)
print(f"\nAz atlag gyozlemi szazalek: {winRatioAvaraga:.2f}%")
print(f"{winRatioAvaraga:.2f}% alatt teljesito csapatok:")
printTemsUnderAvarageWiningRatioToConsole(teamsUnderAvarageRatio)
    