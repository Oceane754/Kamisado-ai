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
