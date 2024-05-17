from typing import List

from citizenships import Citizenships
from footballPlayer import FootballPlayer

from fileService import *
from footballPlayerService import *


footballPlayers:List[FootballPlayer] = getFootballPlayersFromFile("adatok.txt")

#1
# A kapusokon kívül mindenkit mezőnyjátékosnak tekintünk.
# Keresse ki a legidősebb mezőnyjátékos vezeték- és utónevét, valamint születési dátumát! (Feltételezheti, hogy csak egy ilyen játékos van.)
oldestFootballPlayer = getOldestFeildPlayer(footballPlayers)
print(f"\nLegidősebb mezőnyjátékos:")
print(f"{oldestFootballPlayer.firstName} {oldestFootballPlayer.lastName} ({oldestFootballPlayer.birthDate.year}-{oldestFootballPlayer.birthDate.month}-{oldestFootballPlayer.birthDate.day})")
    
#2
# Határozza meg hány magyar, külföldi és kettős állampolgárságú játékos van!
citizenships: Citizenships = getPlayersCitizenship(footballPlayers)
print(f"\nKettos allampolgaraok szama: {citizenships.both}")
print(f"Csak magyar allampolgaraok szama: {citizenships.onlyHungarian}")
print(f"Kulfodli allampolgaraok szama: {citizenships.onlyForegin}")

#3
# Határozza meg játékosok összértékét csapatonként és írja ki a képernyőre!
# A csapatok neve és a játékosainak összértéke jelenjen meg!
print("\nJátékosok összértéke csapatonként:")
playersValueByTeams: Dict[str, int] = getPlayersValueByTeams(footballPlayers)
printPlayersValueByTeams(playersValueByTeams)

#4
# Keresse ki, hogy mely csapatoknál mely posztokon van csupán egy szerződtetett játékos!
# Írja ki a csapat nevet és a posztot amire csak egy játékost szerződtettek!
print("\nCsapatok es posztok amire csak egy játékost szerződtettek:")
teamsWhereOnlyOnePlayerIsOnPosition: Dict[str, List[str]] = getTeamsWhereOnlyOnePlayerIsOnPosition(footballPlayers)
printTeamsWhereOnlyOnePlayerIsOnPosition(teamsWhereOnlyOnePlayerIsOnPosition)

# 5
# Keressük ki azon játékosokat, akiknek az értékük nem haladja meg a játékosok értékének átlag értékét
print("\nJátékosokat akiknek az értékük nem haladja meg a játékosok értékének átlag értékét:")
playersUnderAvarageWorth: List[FootballPlayer] = getPlayersUnderAvarageWorth(footballPlayers)
printPlayersUnderAvarageWorth(playersUnderAvarageWorth)

#6
# Írja ki azon játékosok nevét, születési dátumát és csapataik nevét, akik 18 és 21 év közt vannak és magyar állampolgárok.
# Ha nincs ilyen, akkor megfelelő üzenettel helyettesítse a kimenetet.
hungarianPlayersBetween18And21Age: List[FootballPlayer] = getHungarianPlayersBetween18And21Age(footballPlayers)
printHungarianPlayersBetween18And21Age(hungarianPlayersBetween18And21Age)

#7
# A „hazai.txt” illetve a „legios.txt” állományokba keresse ki a magyar, illetve a külföldi állampolgárságú játékosokat csapatonként.
# A szöveges állományoknak tartalmazniuk kell a csapat nevét majd alatta felsorolva a játékosok teljes nevét, poszt nevet és értéküket.
hungarianFootballPlayers: Dict[str, List[FootballPlayer]] = getPlayersWithHungarianCitizenship(footballPlayers)
hungarianFootballPlayersFileCreated: bool = writeFootballPlayersToFile("hazai.txt", hungarianFootballPlayers)
printFileResultToConsole("hazai.txt", hungarianFootballPlayersFileCreated)

foreignFootballPlayers: Dict[str, List[FootballPlayer]] = getPlayersWithForeignCitizenship(footballPlayers)
foreignFootballPlayersFileCreated: bool = writeFootballPlayersToFile("legios.txt", foreignFootballPlayers)
printFileResultToConsole("legios.txt", hungarianFootballPlayersFileCreated)