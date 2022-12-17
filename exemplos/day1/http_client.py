import socket

# definindo socket a ser usado pelo cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conectando
client.connect(("example.com", 80))

# request (pedido)
cmd = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode()

# envia o pedido
client.send(cmd)

# printa na console response (resposta)
while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

# encerrando o socket
client.close()
