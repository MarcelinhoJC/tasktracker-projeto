# Imagem base leve com Python
FROM python:3.11-slim

# Pasta central de operacoes dentro do container
WORKDIR /app

# Garante saida imediata (sem buffer) no terminal
ENV PYTHONUNBUFFERED=1

# Copia o codigo-fonte local para dentro do container
COPY src/ /app/src/

# Comando que dispara a execucao da aplicacao
CMD ["python", "src/main.py"]
