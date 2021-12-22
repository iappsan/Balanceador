import socket

HOST = '127.0.0.1'      # El hostname o IP del servidor
BUFFERSIZE = 1024           # Tamano del buffer
MYSOCKET = socket.socket()  # Iniciamos el socket

def main():
    global MYSOCKET
    global HOST
    PORT = input("Introduce el puerto para iniciar este servidor: \n")
    MYSOCKET.bind((HOST, PORT)) # Lo ligamos al host y al puerto

    while True:
        print(f'Servidor {HOST} en espera ... ')
        CONN, ADDR = MYSOCKET.accept()      # En espera de cliente
        print (f'{ADDR} conectado!')
        CONN.send(str.encode(f"Estas conectado a {HOST}:{PORT}"))

if __name__ == '__main__':
    main()