from socket import *

srvport = 12345
srv_socket = socket(AF_INET, SOCK_DGRAM)
srv_socket.bind(('', srvport))

print('Ready to receive')
while True:
    msg, client_address = srv_socket.recvfrom(64)
    msg_modified = msg.decode().upper()
    srv_socket.sendto(msg_modified.encode(), client_address)
