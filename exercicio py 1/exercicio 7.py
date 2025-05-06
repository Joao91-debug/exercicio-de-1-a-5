def conversor_moeda():
    try:
        
        reais = float(input("Digite o valor em reais (R$): "))

        cotacao_dolar = 5.20
        
        dolares = reais / cotacao_dolar
        
    
        print(f"R${reais:.2f} equivalem a US${dolares:.2f}")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

conversor_moeda()