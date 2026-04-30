from strategie import choose_move

def afficher(board):
    print("\n")
    for i in range(8):
        ligne = ""
        for j in range(8):
            case_color, piece = board[i][j]
            if piece is None:
                ligne += ". "
            else:
                couleur, joueur = piece
                if joueur == "dark":
                    ligne += "D "
                else:
                    ligne += "L "
        print(ligne)
    print("\n")


# plateau 8x8 avec couleurs (simplifié)
colors = ["orange", "blue", "green", "red", "yellow", "purple", "brown", "pink"]

board = []
for i in range(8):
    row = []
    for j in range(8):
        row.append([colors[(i+j) % 8], None])
    board.append(row)

# IA (dark)
board[7][0][1] = ["orange", "dark"]
board[7][1][1] = ["blue", "dark"]
board[7][2][1] = ["green", "dark"]
board[7][3][1] = ["red", "dark"]

# TOI (light)
board[0][0][1] = ["orange", "light"]
board[0][1][1] = ["blue", "light"]
board[0][2][1] = ["green", "light"]
board[0][3][1] = ["red", "light"]

state = {
    "board": board,
    "current": 1,   # toi commence
    "color": None
}

while True:
    afficher(board)

    if state["color"]:
        print("Couleur imposée:", state["color"])

    if state["current"] == 1:
        print("TON TOUR")

        try:
            x1 = int(input("from x: "))
            y1 = int(input("from y: "))
            x2 = int(input("to x: "))
            y2 = int(input("to y: "))
        except:
            print("Entrée invalide")
            continue

        move = {"from": [x1, y1], "to": [x2, y2]}

    else:
        print("IA JOUE...")
        move = choose_move(state)
        print(move)

    x1, y1 = move["from"]
    x2, y2 = move["to"]

    piece = board[x1][y1][1]

    if piece is None:
        print("❌ pas de pièce ici")
        continue

    # déplacement
    board[x2][y2][1] = piece
    board[x1][y1][1] = None

    # couleur imposée
    state["color"] = board[x2][y2][0]

    # victoire
    if piece[1] == "dark" and x2 == 0:
        print("🔥 IA GAGNE")
        break
    if piece[1] == "light" and x2 == 7:
        print("🔥 TU GAGNES")
        break

    # changer joueur
    state["current"] = 1 - state["current"]