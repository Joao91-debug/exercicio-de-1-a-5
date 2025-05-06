def calcular_total_combustivel():
    preco_gasolina = 5.59
    preco_alcool = 4.39
    preco_diesel = 5.99

    print("Escolha o tipo de combustível:")
    print("1 - Gasolina")
    print("2 - Álcool")
    print("3 - Diesel")
    
    tipo_combustivel = int(input("Digite o número correspondente ao combustível: "))
    litros = float(input("Digite a quantidade de litros abastecidos: "))
    
    if tipo_combustivel == 1:
        total = litros * preco_gasolina
        print(f"Total a pagar pela Gasolina: R$ {total:.2f}")
    elif tipo_combustivel == 2:
        total = litros * preco_alcool
        print(f"Total a pagar pelo Álcool: R$ {total:.2f}")
    elif tipo_combustivel == 3:
        total = litros * preco_diesel
        print(f"Total a pagar pelo Diesel: R$ {total:.2f}")
    else:
        print("Tipo de combustível inválido. Por favor, escolha 1, 2 ou 3.")

calcular_total_combustivel()