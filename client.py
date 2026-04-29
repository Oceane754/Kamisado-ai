import socket
import json
import struct
import protocol
import strategie

def envoyer_message(sock, message_dict):
    message_bytes = json.dumps(message_dict).encode('utf-8')
    taille = len(message_bytes)
    taille_bytes = struct.pack('<I', taille) # Encodage de la taille en 4 bytes
    sock.sendall(taille_bytes + message_bytes)

def recevoir_message(sock):
    raw_size = sock.recv(4)
    if not raw_size:
        return None
        
    taille = struct.unpack('<I', raw_size)[0]
    message_bytes = sock.recv(taille)
    return json.loads(message_bytes.decode('utf-8'))

def inscription(server_ip, server_port, client_port, nom_ia, matricules):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(f"Tentative de connexion au serveur {server_ip}:{server_port}...")
        client_socket.connect((server_ip, server_port))
        print("Connectée ! Envoi de l'inscription...")
        
        # On utilise protocol.py pour fabriquer le formulaire d'inscription
        requete_inscription = protocol.make_subscribe_message(client_port, nom_ia, matricules)
        envoyer_message(client_socket, requete_inscription)
        
        reponse = recevoir_message(client_socket)
        print(f"Réponse du serveur : {reponse}")

def lancer_ecoute(client_ip, client_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ecoute_socket:
        ecoute_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ecoute_socket.bind((client_ip, client_port))
        ecoute_socket.listen()
        print(f"Notre IA est sur écoute sur le port {client_port}...")
        
        while True:
            conn, adresse = ecoute_socket.accept() # Connection spécifique entre le serveur et notre IA
            with conn:
                requete = recevoir_message(conn)
                
                if requete:
                    type_requete = requete.get("request")
                    
                    if type_requete == "ping":
                        reponse = protocol.make_pong_message()
                        envoyer_message(conn, reponse)
                        print("<-- Réponse 'pong' envoyée !")
                        
                    elif type_requete == "play":
                        print("Le serveur me demande de jouer !")
                        etat_du_jeu = requete.get("state")
                        mon_coup = strategie.choose_move(etat_du_jeu)
                        pass
                        
                        response = protocol.make_move_message(mon_coup)
                        envoyer_message(conn, response) 
                        print("<-- Coup envoyé !")