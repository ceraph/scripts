from socket import *
import sys
import getopt

bufsize = 64
srvport = 12345

def udp():
    srv_socket = socket(AF_INET, SOCK_DGRAM)
    srv_socket.bind(('', srvport))

    print('Ready to receive')
    while True:
        msg, client_address = srv_socket.recvfrom(bufsize)
        msg_modified = msg.decode().upper()
        srv_socket.sendto(msg_modified.encode(), client_address)

def tcp():
    srv_socket = socket(AF_INET, SOCK_STREAM)
    srv_socket.bind(('', srvport))
    srv_socket.listen(1)

    print('Ready to receive')
    while True:
        connection_sock, addr = srv_socket.accept()
        msg_modified = connection_sock.recv(bufsize).decode().upper()
        connection_sock.send(msg_modified.encode())
        connection_sock.close()

try:
    opts, args = getopt.getopt(sys.argv[1:], '', ['udp', 'tcp'])
except getopt.GetoptError as err:
    print(err)
    exit(2)

if len(opts) == 0:
    exit(3)

for opt, arg in opts:
   if opt == "--udp":
       udp()
   elif opt == "--tcp":
       tcp()
