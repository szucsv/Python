from io import open
from typing import *
import os
from absence import Absence

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath)
    return os.path.join(basePath, fileName)

def getAbsencesFromFile(fileName: str) -> List[Absence]:
    absences: List[Absence] = []
    absence: Absence = None
    online: str = None
    data: List[str] = []

    try:
        fullPath: str = getFileFullPath(fileName)

        with open (fullPath, encoding="ansi", mode="r") as file:
            for index, line in enumerate(file):
                if(index == 0):
                    continue

                online = line.strip()
                data = online.split(";")
                absence = Absence()
                absence.name = data[0]
                absence.grade = data[1]
                absence.firstDay = int(data[2])
                absence.lastDay = int(data[3])
                absence.missedClasses = int(data[4])

                absences.append(absence)

    except FileNotFoundError:
        print(f"{fileName} nem található!")
    except Exception as ex:
        print("Hiba történt: ", ex)

    return absences

def printAbsences(fileName: str, absences: List[Absence]) -> bool:
    try:
        fullPath: str = getFileFullPath(fileName)
        index: int = 1

        with open (fullPath, encoding='ansi', mode="a") as file:
            for absence in absences:
                file.write(f"{str(absence)}")

                if(len(absences) != index):
                    file.write("\n")

                index += 1

        return True
    except FileNotFoundError as ex:
        return False