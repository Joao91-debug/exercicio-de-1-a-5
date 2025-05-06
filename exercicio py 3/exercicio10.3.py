def contar_caracteres(palavra):
    vogais = "aeiouAEIOU"
    num_vogais = 0
    num_consoantes = 0
    num_espacos = 0

    for letra in palavra:
        if letra in vogais:
            num_vogais += 1
        elif letra.isalpha():  
            num_consoantes += 1
        elif letra.isspace(): 
            num_espacos += 1

    return num_vogais, num_consoantes, num_espacos

for i in range(3):
    palavra = input(f"Digite a palavra {i + 1}: ")
    vogais, consoantes, espacos = contar_caracteres(palavra)
    
    print(f"\nAnálise da palavra '{palavra}':")
    print(f"Número de vogais: {vogais}")
    print(f"Número de consoantes: {consoantes}")
    print(f"Número de espaços: {espacos}")