def cadastrar_cidades():
    cidades = set() 

    print("Digite 8 nomes de cidades (podem haver repetições):")
    for i in range(8):
        cidade = input(f"Digite o nome da cidade : ").strip().title()
        cidades.add(cidade)  

    print("Número de cidades diferentes cadastradas:", len(cidades))
    print("Conjunto de cidades cadastradas:", cidades)

cadastrar_cidades()