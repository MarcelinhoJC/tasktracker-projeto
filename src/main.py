
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "media": "Média",
    "média": "Média",
    "baixa": "Baixa",
}


def solicitar_titulo():
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def solicitar_prioridade():
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Use exatamente Alta, Média (ou Media) ou Baixa.")


def cadastrar_tarefa(tarefas):

    print("\n--- Cadastrar nova tarefa ---")
    titulo = solicitar_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = solicitar_prioridade()
    data_limite = input("Data limite (ex: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título.......: {tarefa['titulo']}")
        print(f"  Descrição....: {tarefa['descricao']}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite']}")
        print(f"  Status.......: {tarefa['status']}")


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
