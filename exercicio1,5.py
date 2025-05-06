def cadastrar_alunos():
    alunos = []  
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":  
            break
        alunos.append(nome)  
    print("\nAlunos cadastrados:")
    for aluno in alunos:  
        print(aluno)

cadastrar_alunos()