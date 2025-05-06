def cadastro_nomes():
    nomes = []  
    while True:  
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")  
        if nome.lower() == 'sair':  
            break 
        nomes.append(nome)  

    print("\nNomes cadastrados:")
    for n in nomes:
        print(n)
    print(f"\nTotal de nomes cadastrados: {len(nomes)}")

cadastro_nomes()