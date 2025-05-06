def numeros ():

    positivos = 0
    negativos = 0
    zeros = 0
for i in range(6):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1


print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números zeros: {zeros}")
numero()