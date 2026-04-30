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

    assert move[0] == move[1]


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

    