import socket
HOST = '10.10.0.1'     # Endereco IP do Servidor
PORT = 5000              # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair, digite: SAIR\n'
msg = raw_input()
while msg != 'SAIR':
    tcp.send (msg)
    msg = raw_input()
tcp.close()
