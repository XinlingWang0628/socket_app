import socket
# Define the server's address and port
HOST = '127.0.0.1'
PORT= 8001

# Server's name and number
my_str = "Server of Xinling Wang"
my_num = 2

# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
# Bind the server to the specified address and port


# Listen for incoming connections with a backlog of 5
server.listen(5)

while True:
     # Accept incoming connection and get the communication socket and client address
    communication_socket, addr = server.accept()
    print("Server Name: " + my_str)
     # Receive and decode the message from the client
    msg = communication_socket.recv(1024).decode('utf-8')
    client_name = msg[:22]
    client_num = msg[22:]
     # Check if the client's number is within the valid range
    if(int(client_num)>100 or int(client_num)<1):
        print("client enter a number that is not in the range of 1-100, connection ended.")
        communication_socket.close()
        break
    print(f"Client Name: {client_name}")
    print("Server Number is:"+str(my_num))
    print("Client_num is :"+client_num)
    print("Sum is:"+str(my_num+int(client_num)))
    # Prepare the response message and send it to the client
    msg = my_str + str(my_num)
    communication_socket.send(msg.encode('utf-8'))
    communication_socket.close()# Close the communication socket
    print("Connection ended!")
