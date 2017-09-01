class Cliente:
    def __init__(self, host, usuario, senha):
        self.host = host
        self.usuario = usuario
        self.senha = senha

    def conectar(self):
        pass

    def enviar_comando(self, comando):
        pass

clientes = []
clientes.append(Cliente("8.8.8.8", "root", "1"))
clientes.append(Cliente("4.4.4.4", "root", "2"))

for i in clientes:
    i.enviar_comando("ping 8.8.8.8")

