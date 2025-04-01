import socket
import threading

def lidar_com_cliente(conexao):
    try:
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            print(f"Dados recebidos: {dados.decode()}")
            conexao.sendall(b"Recebido: " + dados)
    finally:
        conexao.close()

def iniciar_servidor():
    HOST = '0.0.0.0'  # Escuta em todas as interfaces
    PORT = 65432       # Porta para escutar

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escutando em {HOST}:{PORT}")
# Para encerrar o servidor, pressione Ctrl+C        
        while True:
            conn, addr = s.accept()
            print(f"Conectado por {addr}")
            # Cria uma nova thread para cada cliente
            threading.Thread(target=lidar_com_cliente, args=(conn,)).start()

if __name__ == "__main__":
    iniciar_servidor()

