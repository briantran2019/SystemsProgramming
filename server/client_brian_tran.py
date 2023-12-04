import socket

host = "127.0.0.1"  # The server's hostname or IP address
port = 8000  # The port used by the server

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host, port))

message = input("Message: ")

while message.lower() != "quit":
    print(f"Msg to send: {message}")
    clientsock.send(message.encode())
    data = clientsock.recv(1024).decode()
    print(f"Msg recieved from server: {data}")
    if data == "Invalid Command":
        break
    message = input("Message: ")

clientsock.close()
print("closing connection")