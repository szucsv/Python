import datetime

class Freight:
    def __init__(self) -> None:
        self.id: int = None
        self.timeOfDeparture:datetime.datetime = None
        self.travelTime: int = None
        self.distance:float = None
        self.fare: float = None
        self.tip:float = None
        self.paymentType: str = None