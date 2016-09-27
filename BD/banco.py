import os
import sqlite3

def listar_mensagens():
    cursor.execute("SELECT * FROM mensagens")
    for nome, mensagem in cursor.fetchall():
        print nome, mensagem
    raw_input("Pressione Enter Para Sair")

def adicionar_mensagem():
    nome = raw_input("Nome: ")
    mensagem = raw_input("Mensagem: ")
    sql = "INSERT INTO mensagens(nome, texto) VALUES ('{0}', '{1}')".format(nome, mensagem)
    cursor.execute(sql)
    conexao.commit()
    raw_input("Mensagem Adicionada Com Sucesso")
    
conexao = sqlite3.connect("mensagens.bd")
cursor = conexao.cursor()
cursor.execute("DROP TABLE mensagens")
cursor.execute("CREATE TABLE mensagens(nome VARCHAR, texto VARCHAR)")

op = "null"

while op != "6":
    os.system("clear")
    print '== Banco De Dados de Mensagens =='
    print '1) Adicionar Mensagem'
    print '2) Apagar Mensagem Por Nome'
    print '3) Apagar Todas Mensagens'
    print '4) Listar Mensagens Por Nome'
    print '5) Listar Todas Mensagens'
    print '6) Sair'
    op = raw_input("\nOperacao: ")
    if op == "1":
        adicionar_mensagem()
    elif op == "5":
        listar_mensagens()
