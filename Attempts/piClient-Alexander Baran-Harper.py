#Alexander Baran-Harper: https://www.youtube.com/watch?v=PYBZtV2-sLQ
import socket

host = '#YOUR SERVER IP HERE'
port = 5560 #CHANGE PORT IF THIS ONES USED

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

    
s.close()

