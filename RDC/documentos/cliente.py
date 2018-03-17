import socket

operacao = 'nada...'
while operacao != 'SAIR':
    operacao = raw_input('Operacao: ')
    valor1 = raw_input('Valor1: ')
    valor2 = raw_input('Valor2: ')  
    if operacao != 'SAIR':
        soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soquete.connect(('', 3333))
        soquete.send(operacao + '(99)' + valor1 + '(99)' + valor2)
        print soquete.recv(1024)
