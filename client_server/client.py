from socket import *

srvname = 'localhost'
srvport = 12345
client_socket = socket(AF_INET, SOCK_DGRAM)
msg = 'make me uppercase'
client_socket.sendto(msg.encode(), (srvname, srvport))

msg_modified, srv_address = client_socket.recvfrom(64)
print(msg_modified.decode())

client_socket.close()
