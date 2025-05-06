def solicitar_senha():
    while True:
        senha = input("Digite a senha: ")
        if senha == "senac123":
            print("Acesso liberado")
            break
        else:
            print("Senha incorreta. Tente novamente.")

solicitar_senha()