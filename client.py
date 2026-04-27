import socket
import json
import struct

SERVER_IP = "127.0.0.1"  # L'adresse IP du serveur (localhost = mon propre ordinateur)
SERVER_PORT = 3000 # Le port où le serveur écoute

CLIENT_IP = "127.0.0.1" # L'adresse IP où l'IA écoute
CLIENT_PORT = 8888 # Mon port

def envoyer_message(sock, message_dict):
    message_bytes = json.dumps(message_dict).encode('utf-8')
    taille = len(message_bytes)
    taille_bytes = struct.pack('<I', taille) # Transforme la taille du message en un entier binaire sur 4 octets
    sock.sendall(taille_bytes + message_bytes)

def recevoir_message(sock):
    raw_size = sock.recv(4)
    if not raw_size:
        return None
        
    taille = struct.unpack('<I', raw_size)[0]
    message_bytes = sock.recv(taille)
    return json.loads(message_bytes.decode('utf-8'))

def inscription():
    # Création du socket pour se connecter au serveur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(f"Tentative de connexion au serveur {SERVER_IP}:{SERVER_PORT}...")
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connectée ! Envoi de l'inscription...")
        
        requete_inscription = {
            "request": "subscribe",
            "port": CLIENT_PORT,
            "name": "TLC",
            "matricules": ["23276", "23202"]
        }
        
        # J'utilise ma fonction pour envoyer
        envoyer_message(client_socket, requete_inscription)
        
        # J'attends la réponse du serveur
        reponse = recevoir_message(client_socket)
        print(f"Réponse du serveur : {reponse}")

def lancer_ecoute():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ecoute_socket:
        # Permet de relancer le programme tout de suite
        ecoute_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ecoute_socket.bind((CLIENT_IP, CLIENT_PORT))
        ecoute_socket.listen()
        print(f"Notre IA est sur écoute sur le port {CLIENT_PORT}...")
        
        # Boucle infinie pour écouter en permanence
        while True:
            conn, adresse = ecoute_socket.accept()
            
            with conn:
                # Usage de la connexion spécifique entre le serveur et notre IA
                requete = recevoir_message(conn)
                
                if requete:
                    print(f"--> Message reçu du serveur : {requete}")
                    
                    type_requete = requete.get("request")
                    
                    if type_requete == "ping":
                        reponse = {"response": "pong"}
                        envoyer_message(conn, reponse)
                        print("<-- Réponse 'pong' envoyée !\n")
                        
                    elif type_requete == "play":
                        print("Le serveur me demande de jouer !")
                        pass

# Lancement du code
if __name__ == "__main__":
    inscription()
    lancer_ecoute()