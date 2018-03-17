import socket

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.bind(('', 5555))
soquete.listen(0)

while True:
    conexao, cliente = soquete.accept()
    requisicao = conexao.recv(1024)
    operacao, valor1, valor2 = requisicao.split('(99)')
    if operacao == 'SOMA':
        resultado = int(valor1) + int(valor2)
        conexao.send(str(resultado))
    elif operacao == 'SUBTRACAO':
        resultado = int(valor1) - int(valor2)
        conexao.send(str(resultado))
    else:
        conexao.send('OPERACAO INVALIDA')
    conexao.close()

soquete.close()
