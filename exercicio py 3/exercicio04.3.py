def sistema_de_notas():
    total_alunos = 5
    notas = []
    soma_geral = 0
    alunos_aprovados = 0

    for i in range(total_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas.append(nota)
        soma_geral += nota

    media_geral = soma_geral / total_alunos

    print(f"\nMédia geral da turma: {media_geral:.2f}")

    for i in range(total_alunos):
        media_individual = notas[i]
        print(f"Média do aluno {i + 1}: {media_individual:.2f}")

        if media_individual >= 7:
            alunos_aprovados += 1

    print(f"Quantidade de alunos aprovados: {alunos_aprovados}")

sistema_de_notas()