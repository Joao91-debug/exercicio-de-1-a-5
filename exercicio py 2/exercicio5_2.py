def nome_com_letra_inicial():



    for i in range(5):
        nome = input("Digite o nome #{}: ".format(i + 1))
        nomes.append(nome)

    nomes_com_a = [nome for nome in nomes if nome.lower().startswith('a')]

    print("Nomes que começam com 'A' ou 'a':", nomes_com_a)