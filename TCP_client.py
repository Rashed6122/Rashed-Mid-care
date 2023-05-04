import socket

HOST = 'localhost'
PORT = 5000
client_name = "Clinet of clientName"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_number =  input("please enter an integer between 1 and 100: ")
client_socket.connect((HOST, PORT))
client_socket.send((client_name + "," + client_number).encode())
message = client_socket.recv(1024).decode()
data = message.split(",")
if (int(client_number) > 100):
    client_socket.close()
else:    
    print(f'Server name:   {data[0]},  Client name :   {client_name}')
    print(f'Server number: {data[1]},  Clinet number:  {client_number}')
    print("sum = ", int (data[1])+ int (client_number))
    client_socket.close()
