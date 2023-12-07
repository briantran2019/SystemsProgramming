#!/usr/bin/env python3

import socket


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

    # 2: recv msg from the server
    # (can print the message, it's just acknowledgement that it's waiting for a file)

    # 3: call your read_file function here

    # 4: send the bytes from step 3

    pass


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

    # 2: recv file from the server

    # 3: call your write_file function here

    pass


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

    # 2: recv msg from the server
    # (print the message, it's just acknowledgement that it's waiting for a command to run)

    # 3: The server requested the command to send
    # Prompt user for the command they want to run
    # use `input`

    # 4: encode the user input as the type is str, but we need byte string

    # 5: Now the command is ready to send to the client

    # 6: receive the response for the command and print
    # you can decode the response so it prints in a nice format

    pass


if __name__ == "__main__":
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 8080         # The port used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # TODO connect
    #

    while True:
        # Request input from the user
        cmd = input(
            "Enter a command to perform\n run_command\n upload_file\n download_file\n\ncmd: ")

        # User wants to run a command
        if cmd == b"run_command":
            # TODO update the run_command function
            run_command(s, cmd)

        elif cmd == b"upload_file":
            # TODO update the upload_file function
            upload_file(s, cmd)

        elif cmd == b"download_file":
            # TODO update the download_file function
            download_file(s, cmd)

        elif cmd == b"exit":
            # send cmd to server then break out of loop here
            pass
    s.close()
