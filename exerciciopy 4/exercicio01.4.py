import math

def calculadora_cientifica_simples():
    try:
        numero = float(input("Digite um número: "))

        
        if numero < 0:
            print("Raiz quadrada e logaritmo natural não definidos para números negativos.")
        else:
            print(f"Raiz quadrada de {numero} = {math.sqrt(numero)}")
            print(f"Logaritmo natural de {numero} = {math.log(numero)}")

        
        print(f"Seno de {numero} = {math.sin(numero)}")
        print(f"Cosseno de {numero} = {math.cos(numero)}")

    except ValueError:
        print("Por favor, digite um número válido.")

calculadora_cientifica_simples()