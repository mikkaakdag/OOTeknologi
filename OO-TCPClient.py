from socket import *

serverName = "OO-TCP"   
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    # Sende commands
    sentence = input("Skriv command (Random, Add, Subtract) eller 'done' for at afslutte: ")
    clientSocket.send(sentence.encode())

    if sentence.lower() == "done":
        break

    # Modtage svar fra server
    modifiedSentence = clientSocket.recv(1024).decode()
    print("From Server:", modifiedSentence)

    # Sende tal tilbage
    numbers = input("Skriv to tal adskilt af mellemrum: ")
    clientSocket.send(numbers.encode())

    # Modtag resultatet eller advarsel
    modifiedSentence = clientSocket.recv(1024).decode()
    print("From Server:", modifiedSentence)

clientSocket.close()