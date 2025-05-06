def classificar_temperatura():
    try:
        
        temperatura = float(input("Digite a temperatura em graus Celsius: "))
        
        
        if temperatura < 18:
            print("Frio")
        elif 18 <= temperatura <= 25:
            print("Agradável")
        else:
            print("Calor")
    except ValueError:
        print("Por favor, insira um valor numérico válido para a temperatura.")

classificar_temperatura()