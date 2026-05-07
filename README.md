# Kamisado-ai


L'objectif de ce projet consiste à développer une intelligence artificielle capable de jouer au jeu kamisado à travers un système client-serveur.

L'IA doit pouvoir sélectionner des coups valides et efficaces sans générer de bad moves tout cela en fonction de l'état du jeu.


# Structure du projet

- main.py
- main_rival.py
- client.py
- protocol.py
- strategie.py
- requirements.txt
- test_move.py
- test_strategie.py
- README.md


# Fonctionnement 

Le système repose sur une communication client - serveur:

1) Le client se connecte au serveur via des sockets.
2) Les messages sont échangés au format JSON.
3) À chaque tour, l'état du jeu (state) est reçu.
4) La fonction choose_move(state) analyse le plateau.
3) L'ia renvoie le meilleur coup possible sous forme de coordonnées.



# Bibliothèques utilisées

socket : pour établir la communication avec le serveur (gérer les connexions réseau)

JSON : pour envoyer et recevoir les données 

struct : gérer les données binaires (protocole)
Le module struct est utilisé dans la partie réseau du projet pour gérer le protocole de communication et manipuler les données binaires échangées avec le serveur.

Dans notre ia, seul le module random est utilisé
random : sélection aléatoire de la tour au première tour, lorsqu'aucune couleur n'est imposée, une tour est choisie aléatoirement

Pytest : utilsé pour les coverages des tests 
- 2 fichiers tests pour une couvrance finale de 87% contenant 7 tests internes. 


# Modules du projet :

vous verrez 3 modules 
1) client.py   : responsable de la logique côté client et de la communication avec le serveur 
2) protocol.py  : ce module est respinsable de la création et la gestion des messages (gestion des messages) 
3) strategie.py : logique de l'ia

# Stratégie de l’IA

L’IA repose sur une approche heuristique enrichie par des simulations locales avancée en plusieurs étapes: 

1) Analyse du plateau complet (8x8)
 - identification des tours du joueur courant (dark/light)
 - sélection des tours selon la couleur imposée

2) Production des mouvements réalisables

À chaque tour jouable, l’IA crée tous les mouvements possibles :
- en avant,
- en diagonale à gauche,
- en diagonale à droite.

  La génération s'interrompt dès qu'une limite est franchie :

- sortie de la plateforme,
- choc avec un autre élément.

3) Simulation et filtrage de risque de l'IA :
 
 Avant chaque choix, l’IA évalue les résultats de chaque mouvement pour prévenir les erreurs majeures;

 - anti-blunders (évite les pertes directes)
 - anti-rush (prévient les avancées excessives qui pourraient se retourner contre elle).
 - anticipation simple (évalue la capacité de réaction de l'adversaire au prochain tour)

4) Priorité aux coups gagnants  

Si un coup mène directement à la ligne de victoire, alors il est choisi immédiatement.


5) Sinon, évaluation heuristique des mouvements :
Si aucun coup gagnant n'est accessible, l'IA évalue chaque option en fonction de divers critères 
   - la progression vers l'objectif
   - la proximité de la victoire
   - la mobilité (nombre de coups futures possibles)
   - contrôle stratégique ( centre, colonne)
   - réduction des options adverses

6) Choix final basé sur l’heuristique.

L’IA sélectionne le mouvement avec le meilleur score global, assurant :
- sûreté (évite de perdre instantanées),
- stabilité (maintient des options ouvertes) 




# Installation 

Pour installer le projet, veuillez suivre ces étapes :
 1) Récuperer le repo en utilisant la commande git clone

 2) installer les dépendances requises avec  <pip install -r requirements.tx> 
 
 3) Dans un premier terminal, lancer le serveur <python3 server.py kamisado>

 4) Dans deux autres terminaux distincts, lancez les joueurs <python3 main.py > et <python3 main_rival.py >




# Exécution et déroulement du projet 

    •  Le serveur initialise la partie de Kamisado
    •    Les deux clients se connectent automatiquement
    •    Chaque IA reçoit l’état du jeu en temps réel
    •    Les coups sont calculés et envoyés au serveur jusqu’à la fin de la partie

# Groupe ayant réalisé l'ia

Océane Lumpungu 23202
Nouhayla Belkassmi 23276