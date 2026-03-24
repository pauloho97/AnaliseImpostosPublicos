# Análise de Impostos Públicos

Projeto de TCC utilizando Python, SQL e Docker para análise de dados públicos.

## 📁 Estrutura do Projeto

- **app/**
  - Contém os scripts principais em Python
  - `main.py`: arquivo principal de execução
  - `coleta.py`: responsável por buscar dados de APIs
  - `limpezaCSV`: padroniza e limpa arquivos CSV
  - `analise.py`: realiza tratamento e análise dos dados
  - `__init__.py`: arquivo apenas para tornar a pasta app sendo um módulo 

- **data/**
  - Armazena dados coletados (CSV ou temporários)

- **sql/**
  - Scripts de banco de dados
  - `schema.sql`: criação de tabelas

- **tests/**
  - Testes automatizados do sistema

- **requirements.txt**
  - Lista de bibliotecas Python utilizadas

- **Dockerfile**
  - Define o ambiente da aplicação

- **docker-compose.yml**
  - Orquestra os containers (app + banco)

## 🚀 Tecnologias utilizadas

- Python
- SQL
- Docker

## 📊 Objetivo

Analisar dados públicos de arrecadação e gastos governamentais utilizando dados abertos.