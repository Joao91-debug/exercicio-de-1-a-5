def procurar_nome():
    nomes = ["João", "Maria", "Carlos", "Ana", "Pedro"]  
    nome_procurado = input("Digite o nome que deseja procurar: ")  
    
    if nome_procurado in nomes:  
        print(f"O nome {nome_procurado} está presente na lista.")
    else:
        print(f"O nome {nome_procurado} não está presente na lista.")

procurar_nome()