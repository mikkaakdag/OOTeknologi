from socket import *
import json

serverName = "OO-TCP"   
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    # Input fra bruger
    method = input("Skriv command (Random, Add, Subtract) eller 'done' for at afslutte: ")
    if method.lower() == "done":
        clientSocket.send("done".encode())
        break

    tal1 = input("Skriv tal 1: ")
    tal2 = input("Skriv tal 2: ")

    # Lav JSON string
    request = {
        "method": method,
        "Tal1": int(tal1),
        "Tal2": int(tal2)
    }

    clientSocket.send(json.dumps(request).encode())

    # Modtag svar som JSON
    modifiedSentence = clientSocket.recv(1024).decode()
    response = json.loads(modifiedSentence)

    if "result" in response:
        print("Resultat:", response["result"])
    else:
        print("Fejl:", response.get("error", "Ukendt fejl"))

clientSocket.close()
