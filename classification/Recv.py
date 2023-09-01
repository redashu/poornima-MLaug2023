import socket
# target details
target_ip="172.31.36.111"
target_port=2244
target_socket=(target_ip,target_port)

#creating socket object
mysocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#              denote IPv4 , UDP
# start
mysocket.bind(target_socket)

while True:
    print(mysocket.recvfrom(100))
