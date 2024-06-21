# 361 - HW1

This is my TCP client-server program that asks a user for a vector, adds the servers' vector to it, and returns the sum vector back to the client.

## Compilation
1. Open VScode and split the terminals, or use multiple instances of command line. 
2. Change your directory of both terminal instances to that of which this project folder is saved to
3. In 1 terminal instance, type the following into the command line: 
    * python myTCP-server.py
    * Press ENTER and wait for the servers' terminal instance to display the prompt: The server is ready to receive
4. In the next terminal instance, type the following into the command line:
    * python myTCP-client.py
5. When prompted in the clients' terminal instance, refer to the following example for correct input:
    * (Including the prompt): Input 3 integers (i.e x y z) then press ENTER: 1 2 3
    * 1 2 3 being the x y z components of the clients' vector