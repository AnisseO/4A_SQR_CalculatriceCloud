# 4A_SQR_CalculatriceCloud


<p align="center">
  <img src="https://user-images.githubusercontent.com/93181410/166483696-8a4daae2-d6e3-4a61-b425-f5118cc6e085.png" width="300"/>
  <img src="https://user-images.githubusercontent.com/93181410/210587101-8d27cb1b-14ed-4bad-8c16-a579c4ad7289.png" width="180"/>
</p>

4A IE SQR TP1  
OUTSSAKKI Anisse

## Présentation du projet

La première route (/) renvoie la page d'accueil. Les autres routes (/api/addition, /api/soustraction, /api/multiplication, /api/division) acceptent des requêtes HTTP POST avec deux paramètres x1 et x2 qui représentent les deux nombres à utiliser pour l'opération mathématique.

Chaque route utilise les fonctions correspondantes du fichier [functions.py](https://github.com/AnisseO/4A_SQR_CalculatriceCloud/blob/main/functions.py). pour effectuer le calcul et renvoie un identifiant uuid4 du calcul effectué, qui est généré en appelant la fonction generateID(). L'identifiant est ensuite utilisé pour créer une instance de la classe Calcul du fichier [calcul.py](https://github.com/AnisseO/4A_SQR_CalculatriceCloud/blob/main/calcul.py), qui stocke les détails de chaque calcul effectué.
