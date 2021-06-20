import socket

#o programa servidorUDP deverá ser inicializado primeiro para o correto funcionamento do clienteUDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!!")

host = 'localhost'
porta = 5433
mensagem = 'Podemos fazer uma conexão??'

try:
    print("\nCliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()

    print("\nCliente: " + dados)

finally:
    print("\nCliente: Fechando a  conexão")
    s.close()