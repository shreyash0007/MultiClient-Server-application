import socket

# creating TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

print('[Waiting....] waiting for connection response\n')

# if error occurs while binding then print error message
try:
    # since its a TCP socket so we are using "connect" instead of "bind" to bind IP addr and port number  
    sock.connect(('127.0.0.1', 2005))  
except socket.error as err: 
    print(str(err))

# receiving the first message (welcome message) from server
data = sock.recv(1024)
print(data.decode("utf-8"))

while True:
    # sending message
    Inp = input('\nType the message to be echoed: ')
    if Inp =="EXIT": # if input is EXIT then client gets disconnected from server
        break
    sock.send(str.encode(Inp))

    # recieving echo message
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    

sock.close()