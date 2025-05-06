def gerar_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

while True:
    try:
        numero = int(input("Digite um número para gerar a tabuada: "))
        gerar_tabuada(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

    resposta = input("Você gostaria de gerar outra tabuada? (sim/não): ").strip().lower()
    if resposta != 'sim':
        print("Obrigado por usar o gerador de tabuadas! Até a próxima!")
        break