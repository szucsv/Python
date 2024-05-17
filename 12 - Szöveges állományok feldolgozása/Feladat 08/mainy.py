from absenceService import *
from typing import *
from absence import Absence
from fileService import *

absence:List[Absence]=getFileFullPath("szeptember.csv")

writeAbsenceToConsole(Absence)