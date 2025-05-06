def cadastrar_produtos():
    produtos = {}

    
    for i in range(1, 4):
        nome = input(f"Digite o nome do {i}º produto: ").strip().title()
        while True:
            try:
                preco = float(input(f"Digite o preço do produto '{nome}': R$ "))
                break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        produtos[nome] = preco

    print("\nProdutos cadastrados:")
    for nome, preco in produtos.items():
        print(f"- {nome}: R$ {preco:.2f}")


    media = sum(produtos.values()) / len(produtos)
    print(f"\nPreço médio dos produtos: R$ {media:.2f}")

cadastrar_produtos()