from strategie import choose_move

#test1 ; si ia bloquée 

def test_bloque():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    # tour en haut donc aucun move
    board[0][0] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    assert move is None


#test2 :couleur imposee ; est ce que l'ia choisi bien la couleur imposée pour la tour 

def test_couleur_imposee():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    board[6][3] = ("blue", ("blue", "dark"))
    board[6][4] = ("red", ("red", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": "red"
    }

    move = choose_move(state)

    assert move[0] == [6, 4]



#test 3 ; active la partie danger 
def test_evite_danger():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    # rend la colonne dangereuse (bleue)
    for i in range(8):
        board[i][3] = ("blue", None)

    # ma tour
    board[6][3] = ("blue", ("blue", "dark"))

    # adversaire prêt à gagner
    board[1][3] = ("blue", ("blue", "light"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    # l'IA NE DOIT PAS avancer tout droit
    assert move[1][1] != 3



    # test 1: Si blocage ; l'ia ne bouge pas
    # test 2:couleur imposée; l'ia doit jouer la tour correspondante 

        # environ 31% de coverage = peu de ligne de code tester 
    
    #test 3: evitement du danger; évite de joeur un coup qui permet au rival de gagner

        # environ 92% de coverage


# Analyse
# l'ia est efficace dans les situations testées, mais pourrait être améliorée pour battre les ia randoms

from strategie import choose_move



# TEST 1 : IA bloquée


def test_bloque():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    # tour bloquée tout en haut
    board[0][0] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    # plus aucun move possible
    assert move is None



# TEST 2 : couleur imposée


def test_couleur_imposee():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    board[6][3] = ("blue", ("blue", "dark"))
    board[6][4] = ("red", ("red", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": "red"
    }

    move = choose_move(state)

    # doit choisir la tour rouge
    assert move[0] == [6, 4]



# TEST 3 : évite le danger


def test_evite_danger():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    # colonne dangereuse
    for i in range(8):
        board[i][3] = ("blue", None)

    # ma tour
    board[6][3] = ("blue", ("blue", "dark"))

    # adversaire proche de la victoire
    board[1][3] = ("blue", ("blue", "light"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    # ne doit PAS avancer dans la même colonne
    assert move[1][1] != 3



# TEST 4 : victoire immédiate


def test_win_immediate():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    # tour presque gagnante
    board[1][4] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    # doit atteindre la ligne finale
    assert move[1][0] == 0



# TEST 5 : joueur light


def test_light_player():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    board[1][3] = ("blue", ("blue", "light"))

    state = {
        "board": board,
        "current": 1,
        "color": None
    }

    move = choose_move(state)

    # light avance vers le bas
    assert move[1][0] > 1



# TEST 6 : anti-rush


def test_anti_rush():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    board[6][0] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    # évite un déplacement trop grand
    assert abs(move[1][0] - 6) <= 3


# TEST 7 : bonus centre

def test_bonus_centre():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    board[6][1] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    # préfère le centre
    assert 2 <= move[1][1] <= 5