#!/usr/bin/env python3

import socket, os
from subprocess import Popen as popen, PIPE
from command import Command
from fileio import FileIO
# import your modules

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def run_command_server_method(cmd: bytes) -> bytes:
    '''
        Use your Command module here and
        return the results.
    '''
    return Command.run_command_method(cmd)


def upload_file(filename='server_upload.txt') -> None:
    '''
        The server has received the "download_file" command.
        This means the client is trying to download a file from the server.
        The server will upload thie file.

        Use your FileIO module to read the file contents and return the contents
    '''

    # 1: call your read_file function
    # you can use the default filename above
    read = FileIO.read_file(filename)
    # 2: return results
    return read


def download_file(data: bytes, filename='server_download.txt') -> None:
    '''
        The server has received the "upload_file" command.
        This means the server should download the file from the client

        Use your FileIO module to write the file contents
    '''

    # 1: call your write_file function here
    FileIO.write_file(data, filename)
    # you can use the default filename above


if __name__ == "__main__":
    # The server should listen for data from the client and should determine
    # what functions to run based on what the client requested

    s = socket.socket()          # Create a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = '127.0.0.1'
    port = 8000                  # Reserve a port for your service.

    # TODO
    # write code for bind, listen
    s.bind((host, port))
    s.listen()
    # accepting clients
    conn, addr = s.accept()

    # Update the logic to handle the different cases.
    print(f"Connected to client: {addr}")
    count = 0
    while True:
        count += 1
        cmd = conn.recv(4096)
        print(f"Command {count}: {cmd.decode()}")
        # 1.) run_command
        if cmd == b'run_command':
            # Initial message to ask the command
            conn.send('What command would you like to run?'.encode())
            # The client should recv the message and server just waits
            # for the incomming message
            client_cmd = conn.recv(4096)
            # This gets sent to our run command function
            result = run_command_server_method(client_cmd)
            # The run command results are sent back to the client
            conn.send(result)

        # 2.) upload_file
        elif cmd == b'upload_file':
            # The client wants to upload a file
            # Which means the server should download a file sent by the client

            # 1.) send acknowledgement to the client
            # example: s.sendall(b"Waiting for the file")
            conn.send("Waiting for the file.".encode())
            # 2.) Recv the data
            content = conn.recv(4096)
            # # 3.) call the download_file function
            download_file(content)
            conn.send("File received.".encode())
            
        # 3.) download_file
        elif cmd == b'download_file':
            # The client wants to download a file
            # Which means the server should upload a file to send to the client

            # 1.) Call upload function
            result = upload_file()
            # 2.) Send the results back to the client
            conn.send(result)

        # 4.) exit
        elif cmd == b'exit':
            # use `break` to exit loop
            break
        if not conn or not cmd:
            break
    print("closing connection")
    conn.send("close".encode())
    conn.close()
