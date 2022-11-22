from time import sleep
from threading import Thread

def imprimir(identificacao, repeticoes):
    for i in range(repeticoes):
        print("Funcao ", identificacao, ": ", i)
        sleep(1)

linha_execucao1 = Thread(target=imprimir, args=(1, 10))
linha_execucao1.start()

linha_execucao2 = Thread(target=imprimir, args=(2, 10))
linha_execucao2.start()

linha_execucao3 = Thread(target=imprimir, args=(3, 10))
linha_execucao3.start()
