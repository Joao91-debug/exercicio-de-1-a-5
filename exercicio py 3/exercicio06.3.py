def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

while True:
    print("\nMenu de Operações Matemáticas:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '5':
        print("Saindo do programa. Até logo!")
        break

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        if escolha == '1':
            resultado = somar(num1, num2)
            print(f"O resultado da soma é: {resultado}")
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            print(f"O resultado da subtração é: {resultado}")
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            print(f"O resultado da multiplicação é: {resultado}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"O resultado da divisão é: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")