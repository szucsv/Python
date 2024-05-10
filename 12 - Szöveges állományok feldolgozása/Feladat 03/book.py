from author import Author

class Book:
    def __init__(self,) -> None:
        self.author:Author = None
        self.title:str = None
        self.isbn:int = None
        self.publisher:str = None
        self.publishYear:int = None
        self.price:float = None
        self.theme:str = None
        self.pages:int = None
    
    def __str__(self) -> str:
        return f"{self.author}\t {self.title}\t {self.isbn}\t {self.publisher}\t {self.publishYear}\t {self.price}\t {self.theme}\t {self.pages}\t {self.author.honorar}"
    
   