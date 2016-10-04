import os
import sqlite3

def apagar_por_nome():
    print "## Apagar Mensagens Por Nome ##\n"
    nome = raw_input("Nome: ")
    sql = "DELETE FROM mensagens WHERE nome = '{0}'".format(nome)
    cursor.execute(sql)
    conexao.commit()
    if cursor.rowcount > 0:
        print "{0} Mensagens Apagadas!".format(cursor.rowcount)
    else:
        print "Nenhuma Mensagem Apagada!"
    raw_input("Pressione Enter Para Sair")

def apagar_mensagens():
    print "## Apagar Mensagens ##\n"
    sql = "DELETE FROM mensagens"
    cursor.execute(sql)
    conexao.commit()
    print "Todas Mensagens Apagadas!"
    raw_input("Pressione Enter Para Sair")

def listar_por_nome():
    print "## Listar Mensagens Por Nome ##\n"
    nome = raw_input("Nome: ")
    sql = "SELECT * FROM mensagens WHERE nome = '{0}'".format(nome)
    cursor.execute(sql)
    print "NOME\t\tMENSAGEM"
    for nome, mensagem in cursor.fetchall():
        print "{0}\t\t{1}".format(nome, mensagem)
    raw_input("\n## Pressione Enter Para Sair ##")

def listar_mensagens():
    print "## Listar Mensagens ##\n"
    cursor.execute("SELECT * FROM mensagens")
    print "NOME\t\tMENSAGEM"
    for nome, mensagem in cursor.fetchall():
        print "{0}\t\t{1}".format(nome, mensagem)
    raw_input("\n## Pressione Enter Para Sair ##")

def adicionar_mensagem():
    print "## Adicionar Mensagem ##\n"
    nome = raw_input("Nome: ")
    mensagem = raw_input("Mensagem: ")
    sql = "INSERT INTO mensagens(nome, texto) VALUES ('{0}', '{1}')".format(nome, mensagem)
    cursor.execute(sql)
    conexao.commit()
    raw_input("\n## Mensagem Adicionada Com Sucesso ##\nPressione Enter Para Sair!")
    
conexao = sqlite3.connect("mensagens.bd")
cursor = conexao.cursor()
if not os.path.exists("mensagens.bd"):
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
    os.system("clear")
    if op == "1":
        adicionar_mensagem()
    elif op == "2":
        apagar_por_nome()
    elif op == "3":
        apagar_mensagens()
    elif op == "4":
        listar_por_nome()
    elif op == "5":
        listar_mensagens()
