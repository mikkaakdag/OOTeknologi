from socket import *
import threading
import random
import json

def service(connectionSocket):
    while True:
        data = connectionSocket.recv(1024).decode().strip()
        if not data or data.lower() == "done":
            break

        try:
            request = json.loads(data)   # parse JSON
            method = request.get("method")
            n1 = int(request.get("Tal1"))
            n2 = int(request.get("Tal2"))

            if method == "Random":
                result = random.randint(n1, n2)
            elif method == "Add":
                result = n1 + n2
            elif method == "Subtract":
                result = n1 - n2
            else:
                response = {"error": "Unknown method"}
                connectionSocket.send(json.dumps(response).encode())
                continue

            response = {"result": result}
            connectionSocket.send(json.dumps(response).encode())

        except:
            response = {"error": "Invalid JSON or input"}
            connectionSocket.send(json.dumps(response).encode())

    connectionSocket.close()

# Serveropsætning
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("The JSON server is ready to receive")
while True:
    connectionSocket, adr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()
