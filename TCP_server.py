import socket
import threading

HOST = '0.0.0.0'
PORT = 5000
server_name = "Server of serverName" 
stop = 0
threads = []

print('Server started and listening for connections...')

def thread_client(client_socket, address):
    global stop
    message = client_socket.recv(1024).decode()
    data = message.split(",")
    if (int (data[1]) > 100):
        stop = 1
        print ("the receved number is out of range")
        client_socket.close() 
        return
    server_number = 10
    print(f'Connection from {data[0]} has been established with {server_name}!')
    print (f'Client number is {data[1]}, Server number is {server_number}, and the sum is {int (data[1])+server_number}')
    message = server_name + "," + str(server_number)
    client_socket.send(message.encode())   
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
while not stop:
    if (stop):
        break
    client_socket, address = server_socket.accept()
    thread = threading.Thread(target=thread_client, args=(client_socket, address))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print ("sever closed")
    
    
    








