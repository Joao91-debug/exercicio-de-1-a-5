def classificar_aluno():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        media = (nota1 + nota2 + nota3) / 3
        
        print(f"Média: {media:.2f}")
        
        if media >= 7:
            print("Aprovado")
        elif 5 <= media < 7:
            print("Recuperação")
        else:
            print("Reprovado")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para as notas.")
classificar_aluno()