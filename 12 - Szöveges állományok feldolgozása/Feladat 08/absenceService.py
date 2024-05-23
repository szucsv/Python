
from typing import *
import os
from absence import Absence

def writeAbsenceToConsole(absence:List[Absence]) -> None:
    for Absence in absence:
        print(str(Absence))

