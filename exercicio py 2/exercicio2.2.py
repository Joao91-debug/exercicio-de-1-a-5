def sistema_avaliacao():
    notas = []

    print("Digite as 5 notas do aluno:")

    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Nota {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    media = sum(notas) / len(notas)

    print(f"\nMédia: {media:.2f}")