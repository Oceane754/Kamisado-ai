#lire l'état du jeu au moment t
# fonction principale
def choose_move(state):
    my_towers = state["pieces"]["me"]

    x, y = my_towers[0]

    print("Tour choisie :", x, y)

    new_x = x - 1
    new_y = y

    print("Elle va vers :", new_x, new_y)

    return {
        "from": [x, y],
        "to": [new_x, new_y]
    }


# état fictif
fake_state = {
    "board": [[None for _ in range(8)] for _ in range(8)],
    "pieces": {
        "me": [[6, 0], [6, 1]],
        "opponent": [[1, 0], [1, 1]]
    }
}

# appel de la fonction
choose_move(fake_state)

print("TEST FINI")