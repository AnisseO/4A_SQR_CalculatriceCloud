from calcul import Calcul
from flask import Flask
from uuid import uuid4

app = Flask(__name__)

def generateID(self, x1, x2) -> str:
        uniqueID = str(uuid4()) 
        return uniqueID
    
def addition(self, x1, x2) -> int:
        resultat = x1 + x2
        return resultat
    
def soustraction(self, x1, x2) -> int:
        resultat = x1 - x2
        return resultat
    
def multiplication(self, x1, x2) -> int:
        resultat = x1 * x2
        return resultat
    
def division(self, x1, x2) -> float:
        resultat = x1 / x2
        return resultat
    
        
         