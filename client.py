import socket
import os

SERVER_IP = '192.168.1.8'  # Địa chỉ IP của máy chứa server
SERVER_PORT = 12345
BUFFER_SIZE = 4096

def send_file(file_path, server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    file_info = f"{file_name},{file_size}"
    client_socket.send(file_info.encode('utf-8'))

    with open(file_path, 'rb') as file:
        print(f"Sending {file_name} ({file_size} bytes)...")
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            client_socket.sendall(data)

    print(f"{file_name} sent successfully!")
    client_socket.close()

if __name__ == '__main__':
    file_path = 'C:\\Users\\Hien\\Desktop\\truyen\\test3.mp3'  # Đường dẫn đến file bạn muốn gửi
    send_file(file_path, SERVER_IP, SERVER_PORT)
