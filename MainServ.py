import socket

HOST = '172.16.8.23'      # El hostname o IP del servidor
PORT = 10204                 # El puerto que usa el servidor
BUFFERSIZE = 1024           # Tamano del buffer
MYSOCKET = socket.socket()  # Iniciamos el socket
MYSOCKET.bind((HOST, PORT)) # Lo ligamos al host y al puerto
MYSOCKET.listen(5)          # Definimos el numero de conecciones a escuchar
IP = '127.0.0.1'
PORTLIST = [2030, 2031, 2032, 2033, 2034]
contador = len(PORTLIST)-1

def balancea():
    global IP
    global PORTLIST
    successCon = False
    global contador
    servNotChecked = len(PORTLIST)

    while not successCon and servNotChecked > 0:
        try:
            newSocket = socket.socket()
            newSocket.connect((IP,PORTLIST[contador]))
            newSocket.settimeout(5)
            strRes = newSocket.recv(BUFFERSIZE).decode('UTF-8')
            print (strRes)
            successCon = True
        except Exception as ex:
            successCon = False
        finally:
            if contador == 0:
                contador = len(PORTLIST)-1
            else:
                contador -= 1;
    
    if not successCon:
        return ((False,0))
    else:
        return ((True,PORTLIST[contador]))

def main():
    global MYSOCKET
    global HOST
    global BUFFERSIZE    

    while True:
        print('En espera ... ')
        CONN, ADDR = MYSOCKET.accept()      # En espera de cliente
        print (f'{ADDR} conectado!')
        successCon, port = balancea()
        if successCon:
            CONN.send(str.encode(f'Te puedes conectar al: {port}'))
        else:
            CONN.send(str.encode('Ningun servidor disponible'))



if __name__ == '__main__':
    main()