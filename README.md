# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), desenvolvido em **Python 3**
como entrega intermediária (Fase 2) do **Bootcamp II**.

## Descrição funcional

O TaskTracker permite cadastrar e visualizar tarefas pelo terminal, com
validação das informações digitadas:

- **Título** (obrigatório): entradas vazias ou só com espaços são rejeitadas e o sistema pede novamente.
- **Descrição**: texto livre.
- **Prioridade**: aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`.
- **Data limite**: texto livre ou no formato `DD/MM/AAAA`.
- **Status**: definido automaticamente como `Pendente` no cadastro.

## Menu

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

## Tecnologias

- Python 3.8 ou superior (somente biblioteca padrão, sem dependências externas)
- Git e GitHub para versionamento

## Instalação e execução

```bash
git clone https://github.com/MarcelinhoJC/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

> No Linux/macOS, caso `python` não funcione, use `python3 src/main.py`.

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Autor

Marcelo Augusto de Abreu Santos — Análise e Desenvolvimento de Sistemas
