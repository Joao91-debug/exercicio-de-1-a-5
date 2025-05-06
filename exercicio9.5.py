def verificar_paises():
     
    america_do_sul = {
        "Brasil", "Argentina", "Uruguai", "Paraguai", "Chile", "Bolívia",
        "Peru", "Equador", "Colômbia", "Venezuela", "Guiana", "Suriname",
        "Guiana Francesa"
    }

    for i in range(1, 4):
        pais = input(f"Digite o nome do {i}º país: ").strip().title()
        
        
        if pais in america_do_sul:
            print(f"{pais} pertence à América do Sul.")
        else:
            print(f"{pais} NÃO pertence à América do Sul.")

verificar_paises()