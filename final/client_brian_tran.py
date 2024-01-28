#!/usr/bin/env python3

import socket
from command import Command
from fileio import FileIO

def upload_file(s: socket.socket, cmd: bytes, filename='client_upload.txt') -> None:
    '''
        This function is interaction between client and server.
        You send "upload_file" to the server to put it in a waiting state.
        The server will respond it's waiting for a file.

        Call your FileIO read_file function to read the file contents
        Send the file contents to the server (sendall)
    '''
    # s is the socket, use for s.sendall and s.recv
    
    # 1: send cmd to the server
    s.send(cmd)
    # 2: recv msg from the server
    s.recv(4096)
    # (can print the message, it's just acknowledgement that it's waiting for a file)
    # 3: call your read_file function here
    content = FileIO.read_file()
    # 4: send the bytes from step 3
    print("Client: Sending file.")
    s.sendall(content)
    msg = s.recv(4096)
    print(f"Server: {msg.decode()}")

def download_file(s: socket.socket, cmd: bytes, filename='client_download.txt') -> None:
    '''
        This function is interaction between client and server.
        You send "download_file" to the server to put it in a sending state.
        The server sends the file
        You should recv the data sent by the server
        Call your FileIO write_file function write the data sent by the server
    '''
    # s is the socket, use for s.sendall and s.recv

    # 1: send cmd to the server
    s.send(cmd)
    # 2: reCv file from the server
    data = s.recv(4096)
    # 3: call your write_file function here
    FileIO.write_file(data, filename)
    print("Client: File recieved.")
    return None


def run_command(s: socket.socket, cmd: bytes) -> None:
    '''
        This function is interaction between client and server.
        You send "run_command" to the server to put it in a waiting state.
        The server will respond it's waiting for a command to run.

        This is a simple function that just takes input from a user
        Send the user input (make sure to encode it before sending)
    '''
    # s is the socket, use for s.sendall and s.recv
    # 1: send the cmd to the server
    s.send(cmd)
    # 2: recv msg from the server
    msg = s.recv(4096)
    # (print the message, it's just acknowledgement that it's waiting for a command to run)
    # 3: The server requested the command to send
    # Prompt user for the command they want to run
    # use `input`
    usrin = input(f"Server: {msg.decode()}")
    # 4: encode the user input as the type is str, but we need byte string
    # 5: Now the command is ready to send to the client
    s.send(input.encode())
    # 6: receive the response for the command and print
    msg = s.recv(4096)
    print(f"Server reponse: {msg.decode()}")
    return

def get_command() -> bytes:
    return input(
                 "Enter a command to perform\n run_command\n upload_file\n download_file\n\ncmd: "
                ).encode()


if __name__ == "__main__":
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 8000         # The port used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # TODO connect
    #
    s.connect((host, port))

     
    cmd = get_command()

    while cmd != b'exit':
        # User wants to run a command
        s.send(cmd)
        data = s.recv(4096)
        if data == "":
            break
        if cmd == b"run_command":
            # TODO update the run_command function
            cmdtorun = input("What command would you like to run?\n").encode()
            s.send(cmdtorun)
            data = s.recv(4096)
            print(f'Server:\n{data.decode()}')


        elif cmd == b"upload_file":
            # TODO update the upload_file function
            upload_file(s, cmd)

        elif cmd == b"download_file":
            # TODO update the download_file function
            download_file(s, cmd)

        cmd = get_command()
        
    s.send("exit".encode())
    s.close()
    print("closing connection")