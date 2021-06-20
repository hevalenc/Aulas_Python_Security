import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("\nFalha na conexão!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!!\n")

    HostAlvo = input("Digite o HOST ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("\nCliente TCP conectado com sucesso no HOST: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("\nFalha na conexão!!")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
