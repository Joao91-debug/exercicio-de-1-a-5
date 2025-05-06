def media_notas_turma():
    qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))  
    notas = []  

    for i in range(qtd_alunos):
        nota = float(input(f"Digite a nota do {i+1}º aluno: "))
        notas.append(nota)

    
    media_turma = sum(notas) / len(notas)
    
    alunos_acima_media = sum(1 for nota in notas if nota > media_turma)

    print("\nNotas dos alunos:", notas)
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Quantidade de alunos acima da média: {alunos_acima_media}")


media_notas_turma()