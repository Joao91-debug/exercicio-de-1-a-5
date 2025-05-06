def analisador_de_caracteres():
    frase = input("Digite uma frase: ").strip()

    caracteres_unicos = set(frase)

    print(f"\nQuantos caracteres diferentes existem: {len(caracteres_unicos)}")

    print(f"Os caracteres únicos são: {caracteres_unicos}")

analisador_de_caracteres()