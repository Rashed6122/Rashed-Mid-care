# TCP_server_client_socket_programming
client first accept an integer between 1 and 100 from the keyboard, open a TCP
socket to server and send a message containing (i) a string containing name (e.g.,
“Client of John Q. Smith”) and (ii) the entered integer value and then wait for a sever reply.
server will create a string containing its name (e.g., “Server of John Q. Smith”) and then
begin accepting connections from clients. On receipt of a client message, server
i. print (display) the client’s name (extracted from the received message) and the
server’s name
ii. itself pick an integer between 1 and 100 and display the client’s number, its number, and the sum of those
numbers
iii. send its name string and the server-chosen integer value back to the client
iv. if server receives an integer value that is out of range, it terminate after
releasing any created sockets. and this used to shut down server.
