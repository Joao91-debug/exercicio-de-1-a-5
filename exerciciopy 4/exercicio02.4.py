import random

def simular_dado():
    return random.randint(1, 6)

def main():
    while True:
        input("Pressione Enter para lançar o dado...")
        resultado = simular_dado()
        print(f"Você tirou: {resultado}")
        
        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").strip().lower()
        if jogar_novamente == "não":
            print("Obrigado por jogar!")
            break
simular_dado()
main()
