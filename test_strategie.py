from strategie import choose_move

def test_simple():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]
    board[6][3] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    assert move is not None

    pass

#test 2 ; si ia bloquée 
def test_bloque():
    board = [[("white", None) for _ in range(8)] for _ in range(8)]

    # tour en haut doncaucun move
    board[0][0] = ("blue", ("blue", "dark"))

    state = {
        "board": board,
        "current": 0,
        "color": None
    }

    move = choose_move(state)

    assert move[0] == move[1]