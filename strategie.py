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
    
    if state["color"] is None:
        x, y = random.choice(mes_tours)   # premier coup; choix libre
    else:
        x, y = mes_tours[0]              # ensuite; une seule tour imposée

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

#ANTI-RUSH
    filtered_moves = []

    for move in moves:
        nx, ny = move
        distance = abs(nx - x) + abs(ny - y)

        if (mon_joueur == "dark" and nx == 0) or (mon_joueur == "light" and nx == 7):
            filtered_moves.append(move)
    #limite les déplacements trop longs
        elif distance <= 2:
            filtered_moves.append(move)

        elif distance == 3:
            filtered_moves.append(move)  # optionnel

# fallback si jamais tout est supprimé
    if filtered_moves:
        moves = filtered_moves


#sécurité ; si ma tour est bloquée car pas de case libre devant ni en diagonale :
    if not moves:   
        return [[x, y], [x, y]]#correction du bug qui terminait la partie dès que j'étais bloqué !!!
    
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
                directions_adv = [(1, 0), (1, -1), (1, 1)]
                objectif_adv = 7
            else:
                directions_adv = [(-1, 0), (-1, -1), (-1, 1)]
                objectif_adv = 0



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
                        tx += dx
                        ty += dy
                        continue
                        
                    # Adversaire bloqué par une pièce
                    elif plateau[tx][ty][1] is not None:
                        break

                    # Adversaire atteint son objectif
                    if tx == objectif_adv:
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


        # éviter ligne dangereuse
        if mon_joueur == "dark" and nx == 1:
            score -= 400
        elif mon_joueur == "light" and nx == 6:
            score -= 400

        distance = abs(nx - x)
        #empêcher les gros rushs
        if distance >= 3:
            score -= 200
        elif distance == 2:
            score -= 40

        distance = abs(nx - x) + abs(ny - y)       
        score -= distance * 15

        # éviter d'aller trop près de la fin trop tôt
        if mon_joueur == "dark" and nx <= 1:
            score -= 250
        elif mon_joueur == "light" and nx >= 6:
            score -= 250

        #contrôle de colonne (pour bloquer le rival )

        colonne = ny
        pieces_dans_colonne = 0

        for i in range(8):
            if plateau[i][colonne][1] is not None:
                pieces_dans_colonne += 1

        # bonus si colonne "bloquée"
        score += pieces_dans_colonne * 10

        #bonus centre (contrôle stratégique)
        if 2 <= ny <= 5:
            score += 20
        else:
             score -= 10

        if pieces_dans_colonne <= 1:
            score -= 80   # colonne trop ouverte = danger


# un move = [x,y], un second move = [x1,y1], ... et l'ia selon l'ordre logique va choisir le best move
#score= progression + bonus + mobilité 

        # progression : avancer vers la victoire 
        if mon_joueur == "dark":
            score += 1*(7 - nx)
        else:
            score += 1*nx


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

        score += nb_options*3

        if nb_options == 0:
            score -= 1000   # interdit
        elif nb_options <= 2:
            score -= 120

        free_forward = 0

        for dx, dy in directions:
            step = 1
            while True:
                tx = nx + dx * step
                ty = ny + dy * step

                if tx < 0 or tx > 7 or ty < 0 or ty > 7:
                 break

                if plateau[tx][ty][1] is not None:
                    break

                free_forward += 1
                step += 1

        score += free_forward * 5

        if free_forward <= 2:
            score -= 150

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
                        break
            if tour_adverse:
                break 
        nb_moves_adv = 0

        if tour_adverse:
            ax, ay = tour_adverse


            #anticipation simple :est-ce que je serai bien après?

            mon_futur = 0

            for dx, dy in directions:
                step = 1
                while True:
                    tx = nx + dx * step
                    ty = ny + dy * step

                    if tx < 0 or tx > 7 or ty < 0 or ty > 7:
                        break

                    if plateau[tx][ty][1] is not None:
                        break

                    mon_futur += 1
                    step += 1

        # bonus si j’ai encore des options après
            score += mon_futur * 4


            if mon_futur == 0:
                score -= 500   # mort directe
            elif mon_futur <= 2:
                score -= 100

            #éviter de donner une tour trop avancée
            if mon_joueur == "dark" and ax >= 5:
                score -= 150
            elif mon_joueur == "light" and ax <= 2:
                score -= 150

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

            score -= 6 * nb_moves_adv

            if nb_moves_adv >= 6:
                score -= 100   #DANGER: adversaire trop libre

# piege ; creer des mauvais coups pour le rival

        if tour_adverse:
            if nb_moves_adv == 0:
                score += 180   # fort bonus
            elif nb_moves_adv <= 2:
                score += 60
            else:
                score -= nb_moves_adv   #sinon si trop libre: à éviter 
   
        #bloc pour forcer une tour loin de son objectif
            if mon_joueur == "dark":
                score += (7 - ax)
            else:
                score += ax


        if score > best_score:
                best_score = score
                best_move = move


    if best_move:
        return [[x, y], best_move]

    # sinon on ne bouge pas (cas bloqué)
    return [[x, y], [x, y]]



