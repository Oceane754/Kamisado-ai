import client


SERVER_IP = "127.0.0.1" 
SERVER_PORT = 3000      

CLIENT_IP = "127.0.0.1" 
CLIENT_PORT = 8888      

NOM_IA = "TLC"
MATRICULES = ["23276", "23202"]

if __name__ == "__main__":
    print("Démarrage de l'IA...")
    
    # Inscription auprès du serveur
    client.inscription(SERVER_IP, SERVER_PORT, CLIENT_PORT, NOM_IA, MATRICULES)
    
    # Lancement de l'écoute pour recevoir les requêtes du serveur
    client.lancer_ecoute(CLIENT_IP, CLIENT_PORT)