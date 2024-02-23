import socket

# Define the server's address and port
HOST = '127.0.0.1'
PORT = 8001

# User input: client's name and number
my_str = 'Client of Xinling Wang'
my_num = input("please enter a number between 1-100:")

# Create a socket object for communication
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT)) # Connect to the server

# Send the message to the server
msg = my_str + ' ' + str(my_num)    
socket.send(msg.encode('utf-8')) 

# Check if the entered number is within the valid range
if(int(my_num)<=100 and int(my_num)>=1):
    # Receive and decode the server's response
    msg = socket.recv(1024).decode('utf-8')
    server_name = msg[:22]
    server_num = msg[22:]
    print("Client name: "+ my_str+"\nServer name: "+server_name+"\nClient number: "+str(my_num)+"\nServer number: "+server_num+"\nSum is: "+str(int(my_num)+int(server_num)))
else:
    print("client enter a number that is not in the range of 1-100, server has been shut down.")

