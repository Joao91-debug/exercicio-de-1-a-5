def verificar_acesso():
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Entrada permitida. Bem-vindo à festa!")
        else:
            print("Entrada negada. Você precisa ter 18 anos ou mais.")
    except ValueError:
        print("Por favor, digite um número válido para a idade.")

# Chamada da função
verificar_acesso()