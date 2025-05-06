import os

def organizador_de_pastas():
    nome_pasta = input("Digite o nome da nova pasta: ")


    try:
        os.mkdir(nome_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso!")
    except FileExistsError:
        print(f"A pasta '{nome_pasta}' já existe.")
    except Exception as e:
        print(f"Erro ao criar a pasta: {e}")

    print("\nConteúdo do diretório atual:")
    for item in os.listdir():
        print("📁" if os.path.isdir(item) else "📄", item)


organizador_de_pastas()