def make_subscribe_message(port, name, matricules):
    # Préparation de notre formulaire d'inscription
    return {
        "request": "subscribe",
        "port": port,
        "name": name,
        "matricules": matricules
    }

def make_pong_message():
    # Préparation de la réponse au ping
    return {"response": "pong"}

def make_move_message(move):
    # Préparation de l'envoi de notre coup
    return {
        "response": "move",
        "move": move
    }