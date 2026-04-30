import random

def choose_move(state):
    plateau = state ["board"]   # ici ça récupere le tableau de jeu 

    mon_joueur = "dark" if state["current"] == 0 else "light" #dis si je suis dark(joueur du bas) ou bien light(joueur du haut)
    couleur_imposee = state ["color"]      
    mes_tours = [  ]  #liste pour stocker mes tours

#analyser/parcourir tout le plateau pour trouver toute MES tours
    for i in range(8):
        for j in range(8):
            une_tour = plateau [i][j][1] # récupère la piece sur la case (ou pas None). [couleur case], [couleur tour au dessus], [dark 1/light 0]

            if une_tour is not None:
                color, kind = une_tour 

                if kind == mon_joueur:

                    if couleur_imposee is None or color == couleur_imposee:    #si pas de couleur imposé au premier tour ; je peux jouer n'importe quelle tour
                        mes_tours.append([i,j]) #on stocke sa position
    
    if not mes_tours: #sécurité ; pour pas que ça crash lorsqu'il n'y a aucune tour jouable( aucune qui ne respecte la couleur imposée)
            return [[0, 0], [0, 0]]
    
    if state["color"] is None:           # bloc qui sert à prendre un coup intelligent,avantage au début de partie: choisir la meilleure tour
        x,y = mes_tours[0] # initialisation avec la première tour trouvée
        meilleur_progres = float('-inf')

        for i, j in mes_tours:

            if mon_joueur == "dark":
                progres = 7 - i     # car joueur qui doit aller en haut
            else:
                progres = i         # car joueur light va vers le bas

            if progres > meilleur_progres:
                meilleur_progres = progres
                x,y = i,j # on garde la position de la tour qui a le meilleur progès vers la victoire

    else:
        x, y = mes_tours[0] # sinon on prend la première tour trouvée respectant la couleur imposée



    moves = []  # création d'une liste pour les mouvements possibles

# directions diagonale possibles 
    if mon_joueur == "dark":
        directions = [(-1, 0), (-1, -1), (-1, 1)] # avant, diagonale gauche, diagonale droite
    else:
        directions = [(1, 0), (1, -1), (1, 1)]

    for dx, dy in directions:   # génerer des moves
        step = 1

        while True:
            nx = x + dx * step
            ny = y + dy * step

            if nx < 0 or nx > 7 or ny < 0 or ny > 7:
                break

            if plateau[nx][ny][1] is not None:
                break

            moves.append([nx, ny])
            step += 1

#sécurité ; si ma tour est bloquée car pas de case libre devant ni en diagonale :
    if not moves:   
        return [[x, y], [x, y]]
    
    #ici je crée la règle "if i can WIN so I win",
# gagner si possible, pour ne jamais rater une victoire 
    if mon_joueur == "dark":
        objectif = 0
    else:
        objectif = 7

    for move in moves:
        nx, ny = move
        
        if (mon_joueur == "dark" and nx == 0) or (mon_joueur == "light" and nx == 7):
            return[[x, y], move]

 #filtrer les moves dangereux 
    safe_moves = []

    for move in moves:
        nx, ny = move
        # Couleur de la case où l'on atterrit = couleur imposée à l'adversaire
        couleur_donnee = plateau[nx][ny][0]
        
        
        ax, ay = -1,1 # Valeurs par défaut pour éviter problème d'itérabilité
        tour_trouvee = False


        # On cherche la tour adverse de la couleur imposée
        for i in range(8):
            for j in range(8):
                piece = plateau[i][j][1]
                if piece is not None:
                    color, kind = piece
                    if kind != mon_joueur and color == couleur_donnee:
                        ax,ay = i,j
                        tour_trouvee = True
                        break
            if tour_trouvee:
                break
        
        danger = False # vérifie si l’adversaire peut gagner
        
        if tour_trouvee:

            if mon_joueur == "dark":
                directions_adv = [(1, 0), (1, -1), (1, 1)] # Il descend vers 7
                objectif = 7
            else:
                directions_adv = [(-1, 0), (-1, -1), (-1, 1)] # Il monte vers 0
                objectif = 0

            # On simule l'avancée de la tour adverse dans chaque direction
            for dx, dy in directions_adv:
                tx, ty = ax, ay # la position test

                while True:
                    tx += dx
                    ty += dy

                    # Sortie du plateau
                    if tx < 0 or tx > 7 or ty < 0 or ty > 7:
                        break

                    # Collision à notre nouvelle position
                    if tx == nx and ty == ny:
                        break

                    # Adversaire passe par notre ancienne position
                    if tx == x and ty == y:
                        pass
                        
                    # Adversaire bloqué par une pièce
                    elif plateau[tx][ty][1] is not None:
                        break

                    # Adversaire atteint son objectif
                    if tx == objectif:
                        danger = True
                        break
                
                if danger:
                    break

        # On ajoute les safe moves à notre liste
        if not danger:
            safe_moves.append(move)

    # On s'assure de ne faire que des safe moves
    if safe_moves:
        moves = safe_moves
    else:
        pass



#SI je ne peux pas gagner : je calcule un score et je prend le meilleur move
    best_move = None
    best_score = float('-inf') # plusieurs move avec plusieurs scores différents:

    for move in moves:
        nx, ny = move
        score = 0
# un move = [x,y], un second move = [x1,y1], ... et l'ia selon l'ordre logique va choisir le best move
#score= progression + bonus + mobilité 

        # progression : avancer vers la victoire 
        if mon_joueur == "dark":
            score += 2*(7 - nx)
        else:
            score += 2*nx

        # bonus proche de l’arrivée
        if (mon_joueur == "dark" and nx <= 1) or (mon_joueur == "light" and nx >= 6):
            score += 20

        # mobilité : nbr de moves/options possibles depuis la position du point 2 et 1
        
        nb_options = 0 # on commence par compter le nombre de moves possibles

        for dx, dy in directions:
            step = 1
            while True:
                tx = nx + dx * step  #on part d'une position FUTURE ( le move que je teste) "si je vais là? qu'est ce que je peux faire ensuite"
                ty = ny + dy * step


                if tx < 0 or tx > 7 or ty < 0 or ty > 7: #l'ia sort du plateau ; arrêt
                    break

                if plateau[tx][ty][1] is not None:  #si y'a déjà une tour adverse présente sur la case future; arrêt
                    break

                nb_options += 1  # compter les possibilités
                step += 1  

        score += nb_options

        # limiter les moves adverses
        couleur_donnee = plateau[nx][ny][0]

        tour_adverse = None
        for i in range(8):
            for j in range(8):
                piece = plateau[i][j][1]
                if piece is not None:
                    color, kind = piece
                    if kind != mon_joueur and color == couleur_donnee:
                        tour_adverse = (i, j)

        nb_moves_adv = 0

        if tour_adverse:
            ax, ay = tour_adverse

            if mon_joueur == "dark":
                directions_adv = [(1, 0), (1, -1), (1, 1)]
            else:
                directions_adv = [(-1, 0), (-1, -1), (-1, 1)]

            for dx, dy in directions_adv:
                step = 1
                while True:
                    tx = ax + dx * step
                    ty = ay + dy * step

                    if tx < 0 or tx > 7 or ty < 0 or ty > 7:
                        break

                    if plateau[tx][ty][1] is not None:
                        break

                    nb_moves_adv += 1
                    step += 1

        score -= 3*nb_moves_adv

        if score > best_score:
                best_score = score
                best_move = move


    if best_move:
        return [[x, y], best_move]

    # sinon on ne bouge pas (cas bloqué)
    return [[x, y], [x, y]]



