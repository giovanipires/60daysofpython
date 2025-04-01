import socket

HOST = '127.0.0.1'  # Endereço do servidor
PORT = 65432        # Porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ola, servidor!')
    data = s.recv(1024)

print(f"Recebido: {data.decode()}")
