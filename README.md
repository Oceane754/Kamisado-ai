# Kamisado-ai


l'objectif de ce projet consiste à développer une intelligence artificielle capable de jouer au jeu kamisado via un système client-serveur.

Pour cela notre IA doit être capable de choisir des coups valides et efficaces sans générer de bad moves tout cela en fonction de l'état du jeu.


#Structure du projet
.
├── main.py
├── client.py
├── protocol.py
├── strategie.py
├── requirements.txt
└── README.md


# Fonctionnement 


# Bibliothèque utilisé

socket : pour établir la communication avec le serveur (gérer les connexions réseau)

JSON : pour envoyer et recevoir les données 

struct : gérer les données binaires (protocole)

# Modules du projet :

vous verrez 3 modules 
1) client.py   : responsable de la logique côté client et de la communication avec le serveur 
2) protocol.py  : ce module est respinsable de la création et la gestion des messages (gestion des messages) :
3) strategie.py  (logique de l'ia)

## 🧠 Stratégie de l’IA

L’IA fonctionne en plusieurs étapes :

1. Sélection des tours jouables selon la couleur imposée  
2. Génération des déplacements possibles  
3. Filtrage des coups dangereux (évite de donner une victoire directe)  
4. Priorité aux coups gagnants  
5. Sinon, choix du meilleur coup selon :
   - la progression
   - la proximité de la victoire
   - la mobilité

# Installation 

Pour installer le projet, veuillez suivre ces étapes :
 1) dupliquer le repo en utilisant la commande git clone
 2) installer les dépendances requises avec  pip install -r requirements.txt
 3) configurer les paramètres du client et du serveur 

# Exécution du projet 

Pour exécuter le projet, suivez ces étapes :
    1.  Exécuter le fichier main.py avec python main.py.
    2.  Le client s’enregistrera auprès du serveur et établira une connexion.
    3.  Le client enverra et recevra des messages avec le serveur, en utilisant une logique basée sur l’IA pour déterminer la meilleure action à entreprendre.



Pour toute questions, remarque ou retour, veuillez nous contacter à l'adresse suivant : 23276@ecam.be
