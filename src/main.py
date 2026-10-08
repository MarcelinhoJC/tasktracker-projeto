def cadastrar_tarefa(tarefas):
    
    print("\n--- Cadastrar nova tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade: ")
    data_limite = input("Data limite: ")

    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        for campo, valor in tarefa.items():
            print(f"  {campo}: {valor}")


def exibir_menu():
    
    print("\n===== TaskTracker =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():

    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
