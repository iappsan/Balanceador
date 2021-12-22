import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 1020
BUFFERSIZE = 1024
MYSOCKET = socket.socket()

def receive(): # Recibe una actualizacion
    global MYSOCKET
    global BUFFERSIZE
    
    while True:
        try:
            RESPONSE = MYSOCKET.recv(BUFFERSIZE).decode('UTF-8')
            print (RESPONSE)
        except OSError:
            break

def main():
    global MYSOCKET
    global HOST
    global PORT
    MYSOCKET.connect((HOST, PORT))
    keepActive = True

    RECV_THREAD = Thread(target=receive)
    RECV_THREAD.start()

    while keepActive:
        inputStr = input()
        if inputStr == 'exit()':
            keepActive = False
            print('Hasta la vista beibe ;)')
        else:
            print(f'cadena metida: {inputStr}')
            # MYSOCKET.send(str.encode(inputStr))
        
    MYSOCKET.close()

if __name__ == '__main__':
    main()