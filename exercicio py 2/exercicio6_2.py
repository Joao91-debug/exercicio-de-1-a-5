


def calcular_total_com_desconto(valores):
    total = sum(valores)  
    desconto = 0

    
    if total > 200:
        desconto = 0.10  
    elif total > 100:
        desconto = 0.05  

    total_com_desconto = total * (1 - desconto)  
    return total_com_desconto


valores = []
for i in range(4):
    valor = float(input(f"Digite o valor da compra {i + 1}: R$ "))
    valores.append(valor)


total_final = calcular_total_com_desconto(valores)


print(f"O total final com desconto é: R$ {total_final:.2f}")