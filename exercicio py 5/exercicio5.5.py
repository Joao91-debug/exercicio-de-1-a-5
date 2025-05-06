
def exibir_menu():
    print("\n----- Organizador de Tarefas -----")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa (por nome)")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas(tarefas):
    if tarefas:
        print("\nTarefas:")
        for idx, tarefa in enumerate(tarefas, 1):
            print(f"{idx}. {tarefa}")
    else:
        print("Não há tarefas na lista.")

def remover_tarefa(tarefas):
    tarefa_remover = input("Digite o nome da tarefa que deseja remover: ")
    if tarefa_remover in tarefas:
        tarefas.remove(tarefa_remover)
        print(f"Tarefa '{tarefa_remover}' removida com sucesso!")
    else:
        print("Tarefa não encontrada.")

def main():
    tarefas = []
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()