import socket
from threading import Thread

def trata_cliente(cliente):
    mcli = ".."
    mser = ".."
    while (mcli != "sair" or mser != "sair"):
        mcli = cliente.recv(1024).decode()
        if (mcli == "sair"):
            break
        print(mcli)

        mser = input("Mensagem: ")
        cliente.send(mser.encode())
        if (mser == "sair"):
            break
    cliente.close()

PORTA = 3333

servidor = socket.socket()
servidor.bind(("", PORTA))
servidor.listen(5)
print("Servidor escutando na porta: ", PORTA)

while True:
	cliente, endereco = servidor.accept()
	print("Conexao aceita de: ", endereco)

	Thread(target=trata_cliente, args=(cliente,)).start()
	
	
	
	
	
	
	
