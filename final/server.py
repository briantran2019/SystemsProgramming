#!/usr/bin/env python3

import socket
from subprocess import Popen, PIPE

# import your modules


def run_command(cmd: bytes) -> bytes:
    '''
        Use your Command module here and
        return the results.
    '''

    pass


def upload_file(filename='server_upload.txt') -> None:
    '''
        The server has received the "download_file" command.
        This means the client is trying to download a file from the server.
        The server will upload thie file.

        Use your FileIO module to read the file contents and return the contents
    '''

    # 1: call your read_file function
    # you can use the default filename above

    # 2: return results
    pass


def download_file(data: bytes, filename='server_download.txt') -> None:
    '''
        The server has received the "upload_file" command.
        This means the server should download the file from the client

        Use your FileIO module to write the file contents
    '''

    # 1: call your write_file function here
    # you can use the default filename above

    pass


if __name__ == "__main__":
    # The server should listen for data from the client and should determine
    # what functions to run based on what the client requested

    s = socket.socket()          # Create a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = '127.0.0.1'
    PORT = 8080                  # Reserve a port for your service.

    # TODO
    # write code for bind, listen
    #
    #

    # accepting clients
    conn, addr = s.accept()

    # Update the logic to handle the different cases.
    print(f"Connected to client: {addr}")
    while True:
        cmd = conn.recv(4096)
        print(cmd)
        # 1.) run_command
        if cmd == b'run_command':
            # Initial message to ask the command
            conn.sendall(b'What command would you like to run?')
            # The client should recv the message and server just waits
            # for the incomming message
            client_cmd = conn.recv(4096)

            # This gets sent to our run command function
            # make sure to fill it out
            result = run_command(client_cmd)

            # The run command results are sent back to the client
            conn.sendall(result)

        # 2.) upload_file
        elif cmd == b'upload_file':
            # The client wants to upload a file
            # Which means the server should download a file sent by the client

            # 1.) send acknowledgement to the client
            # example: s.sendall(b"Waiting for the file")

            # 2.) Recv the data

            # 3.) call the download_file function
            pass

        # 3.) download_file
        elif cmd == b'download_file':
            # The client wants to download a file
            # Which means the server should upload a file to send to the client

            # 1.) Call upload function
            # 2.) Send the results back to the client
            pass

        # 4.) exit
        elif cmd == b'exit':
            # use `break` to exit loop
            pass

        if not conn:
            break
    conn.close()
    s.close()
