def votacao_candidatos():
    print("Votação entre os candidatos: Ana (1), Bruno (2), Carla (3)\n")

    votos = {"Ana": 0, "Bruno": 0, "Carla": 0}

    for i in range(1, 6):
        while True:
            try:
                voto = int(input(f"Voto {i} - Digite 1 para Ana, 2 para Bruno, 3 para Carla: "))
                if voto == 1:
                    votos["Ana"] += 1
                    break
                elif voto == 2:
                    votos["Bruno"] += 1
                    break
                elif voto == 3:
                    votos["Carla"] += 1
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    print("\nResultado da votação:")
    for candidato, quantidade in votos.items():
        print(f"{candidato}: {quantidade} voto(s)")

votacao_candidatos()