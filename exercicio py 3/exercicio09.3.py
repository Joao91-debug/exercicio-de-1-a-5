import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)  
    tentativas = 3  

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 10. Você tem 3 tentativas.")

    for tentativa in range(tentativas):
        palpite = int(input(f"Tentativa {tentativa + 1}: Insira seu palpite: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite < numero_secreto:
            print("Maior")
        else:
            print("Menor")

    else:
        print("Suas chances acabaram! O número secreto era:", numero_secreto)

jogo_adivinhacao()