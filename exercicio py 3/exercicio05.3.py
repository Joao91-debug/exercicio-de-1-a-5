
def contagem_relogio(horas):
    
    if horas < 0 or horas > 23:
        print("Por favor, insira um número de horas entre 0 e 23.")
        return

    for h in range(horas + 1):

        for m in range(60):
            for s in range(60):
        
                print(f"{h:02}:{m:02}:{s:02}")
                
contagem_relogio(2)