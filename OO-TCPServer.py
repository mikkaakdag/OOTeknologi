from socket import *
import threading
import random

def service(connectionSocket):
    while True:
        # Modtagelse af commands
        command = connectionSocket.recv(1024).decode().strip()
        if command.lower() == "done":
            break

        command = command.capitalize()  # så det passer til "Random", "Add", "Subtract"
        if command in ["Random", "Add", "Subtract"]:
            # Step 2: svar
            connectionSocket.send("Input numbers".encode())
        else:
            connectionSocket.send("Unknown command".encode())
            continue

        # Modtagelse af tal
        numbers = connectionSocket.recv(1024).decode().strip()
        if not numbers:
            connectionSocket.send("Kun tal er tilladt".encode())
            continue

        try:
            n1, n2 = map(int, numbers.split())
        except:
            connectionSocket.send("Invalid numbers".encode())
            continue

        # Beregning
        if command == "Random":
            response = str(random.randint(n1, n2))
        elif command == "Add":
            response = str(n1 + n2)
        elif command == "Subtract":
            response = str(n1 - n2)

        connectionSocket.send(response.encode())
    connectionSocket.close()

# Serveropsætning
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("The server is ready to receive")
while True:
    connectionSocket, adr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()