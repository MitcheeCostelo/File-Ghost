Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import socket
import sys

# Create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print('Creation error: ' + str(msg))

# Binding socket and listen for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print('Binding the port' + str(port))

        s.bind((host, port))
        s.listen(5)
        
    except socket.error as msg:
        print('Socket binding error' + str(msg) + '\n' + 'Retrying ...')
        bind_socket()   


# Establish a connection with client
def socket_accept():
    conn, address = s.accept()
    print('Connection has been established |' + ' IP ' + address[0] + ' | Port ' + str(address[1]))
    send_commands(conn)   
    conn.close()

# Send command to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()   
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))   
            client_response = str(conn.recv(1024), 'utf-8')   
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
