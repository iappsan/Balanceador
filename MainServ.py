import socket

HOST = ''      # El hostname o IP del servidor
PORT = 1020                 # El puerto que usa el servidor
BUFFERSIZE = 1024           # Tamano del buffer
MYSOCKET = socket.socket()  # Iniciamos el socket
MYSOCKET.bind((HOST, PORT)) # Lo ligamos al host y al puerto
MYSOCKET.listen(5)          # Definimos el numero de conecciones a escuchar

def main():
    global MYSOCKET
    global HOST

    print('En espera ... ')
    CONN, ADDR = MYSOCKET.accept()      # En espera de cliente
    print (f'{ADDR} conectado!')
    CONN.send(f"Estas conectado a {HOST}")

if __name__ == '__main__':
    main()