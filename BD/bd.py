import sqlite3

# Conectando ao Banco de Dados (BD) na pasta local.
conexao = sqlite3.connect("mensagens.bd")

# Obtendo o Cursor que e uma instancia de acesso ao BD.
cursor = conexao.cursor()

# Apagando a tabela mensagens se ela existir.
cursor.execute("DROP TABLE IF EXISTS mensagens")
# Apenas com o Commit que os Dados sao escrito fisicamente.
conexao.commit()

# Criando uma nova tabela mensagens.
cursor.execute("CREATE TABLE eita(nome VARCHAR)")
conexao.commit()

# Renomeando o nome da tabela.
cursor.execute("ALTER TABLE eita RENAME TO mensagens")
conexao.commit()

# Criando uma nova tabela mensagens.
cursor.execute("ALTER TABLE mensagens ADD COLUMN texto VARCHAR")
conexao.commit()

# Inserindo uma mensagem no BD.
cursor.execute("INSERT INTO mensagens(nome, texto) VALUES('Charles', 'Ola Mundo')")
cursor.execute("INSERT INTO mensagens(nome, texto) VALUES('Fulano', 'Opa')")
cursor.execute("INSERT INTO mensagens(nome, texto) VALUES('Ciclano', 'Uai')")
conexao.commit()

print "-- Obtendo Todas as Colunas --"
# Obtendo todas as mensagens do BD.
cursor.execute("SELECT * FROM mensagens")
# Imprimindo as mensagens.
print cursor.fetchall()

# Alterando um atributo de um determinado registro.
cursor.execute("UPDATE mensagens SET texto = 'Mudei Agora' WHERE nome = 'Charles'")
conexao.commit()

# Deletando um registro de uma tabela.
cursor.execute("DELETE FROM mensagens WHERE nome = 'Charles'")
conexao.commit()

print "\n-- Obtendo Apenas a Coluna texto --"
# Obtendo todas as mensagens do BD.
cursor.execute("SELECT texto FROM mensagens")
print cursor.fetchall()

# Apagando todas as mensagens do BD.
cursor.execute("DELETE FROM mensagens")
conexao.commit()

print "\n-- Obtendo Todas as Mensagens --"
# Obtendo todas as mensagens do BD.
cursor.execute("SELECT * FROM mensagens")
# Imprimindo as mensagens.
print cursor.fetchall()

# Fechando a conexao com o BD.
conexao.close()

