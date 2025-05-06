def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    if eh_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")