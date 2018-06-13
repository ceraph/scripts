import getopt
import sys
from socket import *

srvname = 'localhost'
srvport = 12345
msg = 'make me uppercase'
msg_modified = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], '', ['tcp', 'udp'])
except getopt.GetoptError as err:
    print(err)
    exit(2)
for opt, arg in opts:
    if opt == '--tcp':
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((srvname, srvport))
        client_socket.send(msg.encode())
        msg_modified = client_socket.recv(64)
        client_socket.close()
    elif opt == '--udp':
        client_socket = socket(AF_INET, SOCK_DGRAM)
        client_socket.settimeout(3)
        client_socket.sendto(msg.encode(), (srvname, srvport))
        msg_modified, srv_address = client_socket.recvfrom(64)
        client_socket.close()
    else:
        assert False, "unhandled option"

print(msg_modified)
