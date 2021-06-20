import socket

#o programa servidorUDP deverá ser inicializado primeiro para o correto funcionamento do clienteUDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!!")

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\nServidor: Vamos junto!!!!'

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem")
        s.sendto(dados + (mensagem.encode()), endereco)
