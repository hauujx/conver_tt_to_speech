import socket
import os

SERVER_IP = '192.168.1.8'
SERVER_PORT = 12345
BUFFER_SIZE = 4096

def receive_file(client_socket):
    file_info = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    file_name, file_size = file_info.split(',')
    file_size = int(file_size)

    with open(file_name, 'wb') as file:
        print(f"Receiving {file_name} ({file_size} bytes)...")
        while file_size > 0:
            data = client_socket.recv(min(BUFFER_SIZE, file_size))
            if not data:
                break
            file.write(data)
            file_size -= len(data)

    print(f"{file_name} received successfully!")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)

    print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection from {client_addr}")
        receive_file(client_socket)
        client_socket.close()

if __name__ == '__main__':
    start_server()