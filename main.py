from flask import Flask, request
from flask_cors import CORS
from calcul import Calcul
from functions import *
import sys

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '''<h1>SALUT</h1>'''

@app.route('/api/addition', methods=['POST'])
def additionRoute():
    x1 = int(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    id = generateID()
    res = addition(x1, x2)
    add = Calcul(id, x1, x2, res)
    return stringID(id)

@app.route('/api/soustraction', methods=['POST'])
def soustractionRoute():
    x1 = int(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    id = generateID()
    res = soustraction(x1, x2)
    sous = Calcul(id, x1, x2, res)
    return id


@app.route('/api/multiplication', methods=['POST'])
def multiplicationRoute():
    x1 = int(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    id = generateID()
    res = multiplication(x1, x2)
    mult = Calcul(id, x1, x2, res)
    return id
    

@app.route('/api/division', methods=['POST'])
def divisionRoute():
    x1 = int(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    id = generateID()
    res = division(x1, x2)
    div = Calcul(id, x1, x2, res)
     
    return id


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)