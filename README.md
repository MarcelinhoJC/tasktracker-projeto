# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), desenvolvido em **Python 3**
para o **Bootcamp II**, agora **conteinerizado com Docker**.

## Descrição funcional

O TaskTracker permite cadastrar e visualizar tarefas pelo terminal, com validação:

- **Título** (obrigatório): entradas vazias ou só com espaços são rejeitadas.
- **Descrição**: texto livre.
- **Prioridade**: aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`.
- **Data limite**: texto livre ou `DD/MM/AAAA`.
- **Status**: definido automaticamente como `Pendente`.

Menu: 1. Cadastrar nova tarefa | 2. Visualizar tarefas | 3. Sair

## Tecnologias

- Python 3.11 (somente biblioteca padrão)
- Docker e Docker Compose
- Git e GitHub

## Executando localmente (sem Docker)

```bash
git clone https://github.com/MarcelinhoJC/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

## Guia Docker

Pré-requisito: [Docker](https://docs.docker.com/get-docker/) instalado e em execução.

### 1. Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

### 3. Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker
```

> O `-it` (ou `stdin_open` + `tty` no Compose) é necessário porque a aplicação
> usa `input()` e precisa de um terminal interativo dentro do container.

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Autor

Marcelo Augusto de Abreu Santos — Análise e Desenvolvimento de Sistemas (Polo Asa Norte)
