# main.py
# Ponto de entrada do projeto
# - Carrega e trata o CSV de saúde usando a função do limpezaCSV.py
# - Exibe algumas informações iniciais para validar a limpeza
# - Para rodar no console: python -m app.main

from app.limpezaCSV import CarregarTratarCsv

def main():
    # Carregar apenas o CSV da saúde
    dfSaude = CarregarTratarCsv("data/despesas_saude_subfuncao.csv", setor="Saúde")

    # Mostrar primeiras linhas para validar
    print("\n--- PRIMEIRAS LINHAS ---")
    print(dfSaude.head())

    # Mostrar últimas linhas
    print("\n--- ÚLTIMAS LINHAS ---")
    print(dfSaude.tail())

    # Mostrar tipos de dados
    print("\n--- TIPOS DE DADOS ---")
    print(dfSaude.dtypes)

if __name__ == "__main__":
    main()
