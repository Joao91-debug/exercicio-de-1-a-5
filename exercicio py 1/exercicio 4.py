
def calcular_pagamento(horas_trabalhadas, valor_hora):
    jornada_normal = 8  
    if horas_trabalhadas > jornada_normal:
        horas_extras = horas_trabalhadas - jornada_normal
        pagamento = (jornada_normal * valor_hora) + (horas_extras * valor_hora * 1.5)
        print(f"Você trabalhou {horas_trabalhadas} horas. Hora extra registrada!")
    else:
        horas_extras = 0
        pagamento = horas_trabalhadas * valor_hora
        print(f"Você trabalhou {horas_trabalhadas} horas.")
    return pagamento

horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor da hora: R$ "))
total = calcular_pagamento(horas, valor)
print(f"Pagamento total: R$ {total:.2f}")