from uuid import uuid4

class Calcul:
    id: uuid4
    x1: int
    x2: int
    resultat: float
    
    def __init__(self, id : uuid4, x1 : int, x2 : int, resultat : float) -> None:
        self.id = id
        self.x1 = x1
        self.x2 = x2
        self.resultat = resultat
        