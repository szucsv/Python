import datetime
import os
from typing import *
from euStateJoinDate import EuStateJoinDate

def getFileFullPath(fileName: str) -> str:
    basePath: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(basePath, fileName)

def getEuStatesWithJoinDateFromFile(fileName: str) -> List[EuStateJoinDate]:
    euStateJoinDates:List[EuStateJoinDate] = []
    oneLine:str = None
    data: List[str] = None
    euStateJoinDate: EuStateJoinDate = None

    try:
        fileFullPath:str = getFileFullPath(fileName)

        with open(fileFullPath, encoding='utf-8', mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(";")

                euStateJoinDate = EuStateJoinDate()
                euStateJoinDate.state = data[0]
                euStateJoinDate.joinDate = datetime.datetime.strptime(data[1], '%Y.%m.%d').date()
                
                euStateJoinDates.append(euStateJoinDate)
    except FileNotFoundError as ex:
        print(f"{ex.fileName} nem található!")

    return euStateJoinDates