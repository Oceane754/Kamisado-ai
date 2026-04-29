import client

SERVER_IP = "127.0.0.1" 
SERVER_PORT = 3000      

CLIENT_IP = "127.0.0.1" 
CLIENT_PORT = 8889 

NOM_IA = "TLC_rival" 
MATRICULES = ["23000", "23207"]

if __name__ == "__main__":
    print("Démarrage de l'IA rivale...")
    
    client.inscription(SERVER_IP, SERVER_PORT, CLIENT_PORT, NOM_IA, MATRICULES)
    
    client.lancer_ecoute(CLIENT_IP, CLIENT_PORT)