def analisador_dados_numericos():
    entrada = input("Digite uma lista de números separados por vírgula (ex: 10, 20, 30): ")
    
    try:
    
        numeros = [float(num.strip()) for num in entrada.split(',')]

        quantidade = len(numeros)
        soma = sum(numeros)
        media = soma / quantidade
        maior = max(numeros)
        menor = min(numeros)

        print("\nAnálise dos Dados:")
        print(f"Quantidade de números: {quantidade}")
        print(f"Soma: {soma}")
        print(f"Média: {media}")
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números separados por vírgula.")


analisador_dados_numericos()