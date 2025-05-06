def cadastrar_senha():
    while True:
        senha = input("Digite sua senha: ")
        confirmacao = input("Confirme sua senha: ")
        
        if senha == confirmacao:
            print("Senha criada com sucesso!")
            break
        else:
            print("As senhas não coincidem. Tente novamente.")

cadastrar_senha()