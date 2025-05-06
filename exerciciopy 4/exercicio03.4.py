from datetime import datetime

def agenda_digital():
    # Mostra a data e hora atual
    agora = datetime.now()
    data_formatada = agora.strftime("Hoje é dia %d/%m/%Y e agora são %H:%M.")
    print(data_formatada)

    # Pergunta se o usuário deseja agendar algo
    resposta = input("Deseja agendar um compromisso? (s/n): ").strip().lower()

    if resposta == 's':
        titulo = input("Digite o título do compromisso: ")
        data = input("Digite a data do compromisso (dd/mm/aaaa): ")

        compromisso = f"{titulo} - {data}"
        print("Compromisso agendado com sucesso!")
        print(">>", compromisso)
    else:
        print("Nenhum compromisso agendado.")

    
agenda_digital()