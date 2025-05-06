def soma_numeros_pares():
    numeros = []  
    for i in range(6):  
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)  
    
    soma_pares = sum(num for num in numeros if num % 2 == 0)  
    
    print(f"A soma dos números pares digitados é: {soma_pares}")

soma_numeros_pares()