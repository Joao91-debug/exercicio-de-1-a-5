def caixa_eletronico(valor):
    cedulas = [100, 50, 20, 10]
    quantidade_cedulas = []

    for cedula in cedulas:
        quantidade = valor // cedula
        valor %= cedula
        quantidade_cedulas.append(quantidade)

    print("Cédulas entregues:")
    for i, cedula in enumerate(cedulas):
        if quantidade_cedulas[i] > 0:
            print(f"R${cedula}: {quantidade_cedulas[i]} cédula(s)")

    if valor > 0:
        print(f"Não é possível sacar R${valor} com as cédulas disponíveis.")
    else:
        print("Saque realizado com sucesso!")

valor_saque = int(input("Digite o valor do saque: R$"))
caixa_eletronico(valor_saque)