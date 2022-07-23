import socket           # Importing socket module
from _thread import *   # Importing thread module

# Create a TCP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the socket to the port
    sock.bind(('127.0.0.1', 2005))
except socket.error as err:     # if error occurs while binding then print the error message
    print(str(err))

# listening 
print('[Listening...]')
sock.listen(5)

print("[Waiting...] waiting for connection")

# Initializing thread count
ThreadCount = 0
connections = 0
flag = False
# defining multi_threaded_client function which takes socket object as parameter



def multi_threaded_client(sock_obj):
    global connections
    global flag
    # sending welcome message to client
    sock_obj.send(str.encode('----Welcome to the Server----\n'))


    while True:
        # receiving data from client
        data = sock_obj.recv(2048)

        # sending echo reply to client
        reply = 'Echoed message by Server: ' + data.decode('utf-8')
        if not data:
            break
        sock_obj.sendall(str.encode(reply))
    
    # closing connection with client
    sock_obj.close()
     

while True:
    # accepting connection for client
    sock_obj, address = sock.accept()
    print('\nConnected to: ', address)

    # Assigning threads to every new client
    start_new_thread(multi_threaded_client, (sock_obj, ))

    # incrementing thread count
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

sock.close()

  
    

