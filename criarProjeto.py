import os

base = "AnaliseImpostosPublicos"

# Estrutura de pastas
pastas = [
    f"{base}/app",
    f"{base}/data",
    f"{base}/sql",
    f"{base}/tests"
]

# Arquivos iniciais
arquivos = {
    f"{base}/app/main.py": "",
    f"{base}/app/coleta.py": "",
    f"{base}/app/analise.py": "",
    f"{base}/sql/schema.sql": "",
    f"{base}/tests/test_analise.py": "",
    f"{base}/requirements.txt": "pandas\nrequests\nsqlalchemy\npytest\n",
    f"{base}/Dockerfile": """FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/main.py"]
""",
    f"{base}/docker-compose.yml": """version: '3.9'
services:
  app:
    build: .
    container_name: tcc_app
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: postgres
    container_name: tcc_db
    environment:
      POSTGRES_PASSWORD: 1234
    ports:
      - "5432:5432"
""",
    f"{base}/README.md": "# Análise de Impostos Públicos\n\nProjeto de TCC utilizando Python, SQL e Docker.\n"
}

# Criar pastas
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)

# Criar arquivos
for caminho, conteudo in arquivos.items():
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)

print("Projeto 'AnaliseImpostosPublicos' criado com sucesso!")