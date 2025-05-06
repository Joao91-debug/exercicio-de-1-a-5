def mostrar_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    while True:
        try:
            num = int(input("Digite um número para ver sua tabuada de 1 a 10: "))
            mostrar_tabuada(num)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        resposta = input("Quer ver outra tabuada? (s/n): ").strip().lower()
        if resposta != 's':
            print("Até mais! Tenha um ótimo dia!")
            break

if __name__ == "__main__":
    main()