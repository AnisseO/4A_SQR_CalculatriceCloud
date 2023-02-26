from calcul import Calcul
from flask import Flask
from uuid import uuid4

app = Flask(__name__)

def generateID() -> uuid4:
        uniqueID = uuid4()
        return uniqueID
    
def addition(x1, x2) -> int:
        resultat = x1 + x2
        return resultat
    
def soustraction(x1, x2) -> int:
        resultat = x1 - x2
        return resultat
    
def multiplication(x1, x2) -> int:
        resultat = x1 * x2
        return resultat
    
def division(x1, x2) -> float:
        resultat = x1 / x2
        return resultat

def stringID(id: uuid4) -> str:
        uniqueID = str(id) 
        response = "<h1>Votre ID : </h1><ul>" + "<li>"  + uniqueID + "</li>"
        return response   
         
def getResultByID(id: str)-> float:
        
        return 