# Importing necessary libraries
from socket import *

# Creating server connections
server = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server,serverPort))

# Asking for user input for the vector
sentence = input('Input 3 integers (i.e x y z) then press ENTER: ')

# Sending the clients' input to the server
clientSocket.send(sentence.encode())

# Setting the recieved string vector from the server to a variable
moddedVI = clientSocket.recv(1024)

# Printing the string vector from the server
print('From Server: ', moddedVI.decode())

# Closing
clientSocket.close()