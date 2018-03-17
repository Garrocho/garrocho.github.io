import socket

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.bind(('', 3333))
soquete.listen(0)

while True:
    conexao, cliente = soquete.accept()
    requisicao = conexao.recv(1024)
    operacao, valor1, valor2 = requisicao.split('(99)')
    if operacao == 'SOMA':
        soqsoma = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soqsoma.connect(('', 4444))
        soqsoma.send(operacao + '(99)' + valor1 + '(99)' + valor2)
        resultado = soqsoma.recv(1024)
        conexao.send(resultado)
        soqsoma.close()
    elif operacao == 'SUBTRACAO':
        soqsub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soqsub.connect(('', 5555))
        soqsub.send(operacao + '(99)' + valor1 + '(99)' + valor2)
        resultado = soqsub.recv(1024)
        conexao.send(resultado)
        soqsub.close()
    else:
        conexao.send('OPERACAO INVALIDA')
    conexao.close()

soquete.close()
