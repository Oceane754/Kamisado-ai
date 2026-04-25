import random

def move(state): 
    possible_moves = state["possible_moves"]    # state = info du jeu
    
    return random.choice(possible_moves)  # choisir une mouvement au hasard
