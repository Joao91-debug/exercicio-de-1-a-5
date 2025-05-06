def verificar_senha():
    senha_correta = "senac123"
    senha = input("Digite a senha para continuar: ")
    
    if senha == senha_correta:
        print("Senha correta! Acesso permitido.")
    else:
        print("Senha incorreta. Acesso negado.")

verificar_senha()