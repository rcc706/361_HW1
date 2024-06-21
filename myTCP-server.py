# Importing necessary libraries
from socket import *

# Setting the server port and server Socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Binding the serverSocket to the port
serverSocket.bind(('',serverPort))

# Sever is listening to only requst
serverSocket.listen(1)

# Declaring empty list for the vectors
sum = [0, 0, 0]
server_default_Vector = [1, 1, 1]

print("The server is ready to receive")

while True: 
    
    # Accepting and decode request from the client
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    
    # Splitting the vector string from the client into separate elements
    arr = sentence.split()
    
    # Adding the default Vector elements to the clients' vector elemnets
    for i in range(3):
        sum[i] = server_default_Vector[i] + int(arr[i])
    
    # Creating the new string vector and sending it to the client
    newVector = str(sum[0]) + " " + str(sum[1]) + " " + str(sum[2])
    connectionSocket.send(newVector.encode())
    
    # Closing
    connectionSocket.close()
    
    # Exiting
    exit()