import platform

def ver():
    print(platform.system())
    print(platform.release())

comando = ""
while comando != "exit":
    comando = input("/> ")
    if comando == "ver":
        ver()
    elif comando != "exit":
        print("Comando Invalido!")
