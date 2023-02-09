from flask import Flask
from calcul import Calcul
from functions import *
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return '''<h1>SALUT</h1>'''

@app.route('/api/addition/<int:x1>/<int:x2>', methods=['POST'])
def additionRoute(x1, x2):
    id = generateID(x1,x2);
    return id

@app.route('/api/soustraction/<int:x1>/<int:x2>', methods=['POST'])
def soustractionRoute(x1, x2):
    id = generateID(x1,x2);
    return id


@app.route('/api/multiplication/<int:x1>/<int:x2>', methods=['POST'])
def multiplicationRoute(x1, x2):
    id = generateID(x1, x2);
    return id
    

@app.route('/api/division/<int:x1>/<int:x2>', methods=['POST'])
def divisionRoute(x1, x2):
    id = generateID(x1,x2);
    return id

@app.route('/api/resultat/<str:id>', methods=['GET'])
def getResult():
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)