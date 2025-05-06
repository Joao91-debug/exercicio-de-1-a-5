from datetime import datetime

def descobrir_dia_da_semana():
    data_str = input("Digite uma data no formato dd/mm/aaaa: ")

    try:
    
        data = datetime.strptime(data_str, "%d/%m/%Y")

        
        dias_semana = [
            "segunda-feira", "terça-feira", "quarta-feira",
            "quinta-feira", "sexta-feira", "sábado", "domingo"
        ]

        dia_semana = dias_semana[data.weekday()]
        print(f"O dia {data_str} cai em uma {dia_semana}.")

    except ValueError:
        print("Formato inválido! Use dd/mm/aaaa.")


descobrir_dia_da_semana()