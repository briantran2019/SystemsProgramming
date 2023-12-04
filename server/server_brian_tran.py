import socket

host = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen()
connection, address = sock.accept()
print(f"Connection from {address[0]}")

while True:
    data = connection.recv(1024).decode()
    print(f"Msg recieved from client: {data}")
    if not data:
        break
    match data:
        case "hello":
            print("Responding with: world")
            data = "world"
        case "quit":
            print("Responding with exit")
            data = "quitting"
            break
        case _:
            print("Invalid command")
            connection.sendall("Invalid Command".encode())
            break
    connection.send(data.encode())
connection.close()
print("closing connection")
