import time

def cronometro():
    try:
        segundos = int(input("Digite o número de segundos para o cronômetro: "))

        print("Iniciando cronômetro...")
        for i in range(segundos, -1, -1):
            print(i)
            time.sleep(1)

        print("Tempo encerrado!")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")


cronometro()