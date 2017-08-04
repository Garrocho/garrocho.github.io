#!/usr/bin/python
# -*- coding: utf-8 -*-
import crypt


def testaSenha(dados):
    senha = dados.split('$')
    salt = '$' + senha[1] + '$' + senha[2]
    dicionario = open('dicionario.txt', 'r')
    for palavra in dicionario.readlines():
        palavra = palavra.strip('\n')
        palavraCriptografada = crypt.crypt(palavra, salt)
        if palavraCriptografada == dados:
            print '[+] Encontrado a Senha: ' + palavra + '\n'
            return
    print '[-] Senha Não Encontrada.\n'
    return


def inicio():
    arquivoSenhas = open('senhas.txt')
    for linha in arquivoSenhas.readlines():
        if ':' in linha:
            dados = linha.split(':')
            print '[*] Quebrando senha de: ' + dados[0]
            testaSenha(dados[1])

if __name__ == '__main__':
    inicio()
