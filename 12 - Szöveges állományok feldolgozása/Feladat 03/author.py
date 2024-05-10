class Author:
    def __init__(self) -> None:
        self.firstName:str = None
        self.lastName:str = None
        self.birthday:str = None
        self.honorar:str = None
    
    def __str__(self) -> str:
        return f"{self.firstName}\t {self.lastName}\t {self.birthday}"