# Arquivo para carregar e tratar os dados do CSV, removendo colunas desnecessárias e convertendo 
# os valores monetários para um formato numérico adequado.
# Também inclui uma função para exibir informações básicas do DataFrame, 
# como as primeiras e últimas linhas, e os tipos de dados.

import pandas as pd

# Função para carregar e tratar o CSV, removendo colunas desnecessárias.
# e convertendo os valores monetários
def CarregarTratarCsvDespesas(caminhoCsv, setor=None):
    dataframe = pd.read_csv(caminhoCsv, sep=";")
    
    # Remover colunas lixo
    dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')]
    
    # Converter valores monetários
    ColunaValores = [
        "Valor Empenhado",
        "Valor Liquidado",
        "Valor Pago",
        "Valor Restos a Pagar Pagos"
    ]
    
    # for para passar por cada coluna de valor, remover pontos e substituir vírgula por ponto, e converter para numérico
    for coluna in ColunaValores:
        dataframe[coluna] = (
            dataframe[coluna]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        dataframe[coluna] = pd.to_numeric(dataframe[coluna], errors="coerce")
    
    # --- MELHORIA: TRATAMENTO DE NULOS ---
    # Converte qualquer valor vazio (NaN) nas colunas de despesa para 0
    # Isso garante que a soma aritmética no SQL ou Pandas funcione corretamente
    dataframe[ColunaValores] = dataframe[ColunaValores].fillna(0)
    # -------------------------------------
    
    # Converter Mês Ano para datetime
    dataframe["MesAno"] = pd.to_datetime(dataframe["Mês Ano"], format="%m/%Y")

    # Adicionar coluna Setor (se informado)
    if setor:
        dataframe["Setor"] = setor
    
    return dataframe

# Função para exibir informações básicas do DataFrame, 
# como as primeiras e últimas linhas, e os tipos de dados.
def MostrarInfoBasica(dataframe, nome_setor="Setor"):
    """Exibe informações básicas de um DataFrame para validação."""
    print(f"\n=== {nome_setor.upper()} ===")
    print("\n--- PRIMEIRAS LINHAS ---")
    print(dataframe.head())
    
    print("\n--- ÚLTIMAS LINHAS ---")
    print(dataframe.tail())
    
    print("\n--- TIPOS DE DADOS ---")
    print(dataframe.dtypes)