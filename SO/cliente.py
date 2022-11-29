import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 3333))

mcli = ".."
mser = ".."
while (mcli != "sair" or mser != "sair"):
    mcli = input("Mensagem: ")
    cliente.send(mcli.encode())
    if (mcli == "sair"):
        break
    
    mser = cliente.recv(1024).decode()
    if (mser == "sair"):
        break
    print(mser)
