def calcular_desconto():
    try:
        valor = float(input("Digite o valor do produto (em R$): "))
        if valor > 100:
            desconto = valor * 0.10
            valor_final = valor - desconto
            print(f"Desconto de R$ {desconto:.2f} aplicado.")
            print(f"Valor com desconto: R$ {valor_final:.2f}")
        else:
            print(f"O produto custa R$ {valor:.2f}. Não há desconto.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

# Chamada da função
calcular_desconto()